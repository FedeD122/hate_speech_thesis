
import json
import pandas as pd

from lftw.components.preprocessing import TARGET_CATS, build_highlight_vector, clean_and_union_spans
from typing import Dict
from pathlib import Path
from pyhighlights.components.loaders import HighlightLoader

class LFTWLoader(HighlightLoader):

    SILVER_ANN = "silver_mistral_fewshot_checked.jsonl"
    GOLD_ANN = "merged_annotations.json"

    def __init__(
        self,
        directory: str,
        target_category: str = None,
        test_file: str = "test.csv",
        **kwargs,
    ):
        super().__init__(directory=directory, **kwargs) 
        self.target_category = target_category
        self.test_file = test_file

    def _parse_label_studio(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            ls_data = json.load(f)
            
        parsed_rows = []
        for task in ls_data:
            text_val = task['data'].get('text', '') 
            row = {"text_ls": text_val}
            
            raw_spans = {cat: [] for cat in TARGET_CATS}
            
            if 'annotations' in task:
                for annotation in task['annotations']:
                    for item in annotation.get('result', []):
                        if item['type'] == 'labels':
                            cat_name = item['value']['labels'][0]
                            text_span = item['value']['text']
                            if cat_name in TARGET_CATS:
                                raw_spans[cat_name].append(text_span)
            
    
            for cat in TARGET_CATS:
                row[cat] = clean_and_union_spans(raw_spans[cat])
                
            parsed_rows.append(row)
            
        return pd.DataFrame(parsed_rows)
    
    def _split_dataset(self):
        train_path = self.directory / "train.csv"
        val_path = self.directory / "val.csv"
        test_path = self.directory / "test.csv"
        test2_path = self.directory / "test2.csv"

        if train_path.exists() and val_path.exists() and test_path.exists() and test2_path.exists():
            return

        main_file = self.directory / "dataset.csv"

        df = pd.read_csv(main_file)
        df = df[df["label"] == "hate"]

        ls_path = self.directory / self.GOLD_ANN
        ls_df = self._parse_label_studio(ls_path)

        df['text_match'] = df['text'].astype(str).str.strip()
        ls_df['text_match'] = ls_df['text_ls'].astype(str).str.strip()

        test2_texts = ls_df['text_match'].tolist()

        mask_test2 = df['text_match'].isin(test2_texts)
        df_test2 = df[mask_test2].copy()
        df_main = df[~mask_test2].copy()

        ls_df = ls_df.drop(columns=['text_ls'])
        df_test2 = df_test2.merge(ls_df, on="text_match", how="left")
        
        df_test2 = df_test2.drop(columns=['text_match'])

        highlights_path = self.directory / self.SILVER_ANN
        if highlights_path.exists():
            hl = pd.read_json(highlights_path, lines=True)
            df_main = df_main.merge(hl[["acl.id"] + TARGET_CATS], on="acl.id", how="left")
            for c in TARGET_CATS:
                df_main[c] = df_main[c].fillna("absent")
        else:
            print(f"[ATTENZIONE] {highlights_path} non trovato.")
            for c in TARGET_CATS:
                df_main[c] = "absent"

        df_main = df_main.drop(columns=['text_match'])

        split_map = {"train": "train", "dev": "val", "test": "test"}
        df_main["split_mapped"] = df_main["split"].map(split_map)
        
        for name, path in (("train", train_path), ("val", val_path), ("test", test_path)):
            df_main[df_main["split_mapped"] == name].drop(columns=["split_mapped"]).to_csv(path, index=False)

        df_test2.to_csv(test2_path, index=False)

    def _formatta(self, df):
        sample_id = range(len(df))
        tokens = df["text"].astype(str).str.split()

        has_categories = all(c in df.columns for c in TARGET_CATS)

        binary_targets = {}
        for c in TARGET_CATS:
            col_name = f"has_{c.lower().replace(' ', '_')}"
            if c in df.columns:
                binary_targets[col_name] = df[c].apply(
                    lambda val: 1 if isinstance(val, str) and val.strip().lower() != "absent" and val.strip() != "" else 0
                )
            else:
                binary_targets[col_name] = pd.Series([0] * len(df))

        for col_name, series in binary_targets.items():
            df[col_name] = series

        if self.target_category is None:
            label_map = {"nothate": 0, "hate": 1}
            labels = df["label"].astype(str).str.lower().str.strip().map(label_map)
            assert labels.notna().all(), f"label non mappate: {df['label'][labels.isna()].unique()}"

            if has_categories:
                highlights = df.apply(
                    lambda row: build_highlight_vector(str(row["text"]), row)
                    if str(row["label"]).strip().lower() == "hate" else None,
                    axis=1,
                )
            else:
                highlights = pd.Series([None] * len(df), dtype=object)

        else:
            col_name = f"has_{self.target_category.lower().replace(' ', '_')}"
            labels = binary_targets[col_name]

            if has_categories and self.target_category in df.columns:
                highlights = df.apply(
                    lambda row: build_highlight_vector(
                        str(row["text"]),
                        row,
                        categories=[self.target_category],
                    )
                    if row[col_name] == 1 else None,
                    axis=1,
                )
            else:
                highlights = pd.Series([None] * len(df), dtype=object)

        result_dict = {
            "sample_id": sample_id,
            "text": df["text"].astype(str),
            "tokens": tokens,
            "label": labels,
            "highlights": highlights,
        }
        result_dict.update(binary_targets)

        return pd.DataFrame(result_dict)

    def read(self):
        self._split_dataset()
        result = {
            "train": self._formatta(pd.read_csv(self.directory / "train.csv", low_memory=False)),
            "val": self._formatta(pd.read_csv(self.directory / "val.csv", low_memory=False)),
            "test": self._formatta(pd.read_csv(self.directory / self.test_file, low_memory=False)),
        }
        for name, df in result.items():
            df.to_csv(self.directory / f"{name}_formatted.csv", index=False)
        return result