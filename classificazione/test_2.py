from pathlib import Path
import torch as th
import lightning as L 
import pandas as pd
import numpy as np

import lftw
import pyhighlights
from cinnamon.registry import Registry, RegistrationKey
from lftw.configurations.keys import (
    LFTW_ETHNICITY_FR_TASK_TEST2, 
    LFTW_SEXOR_FR_TASK_TEST2,
    LFTW_RELIGION_FR_TASK_TEST2,
    LFTW_GENDER_FR_TASK_TEST2,
    LFTW_GENDER_FR_TASK
)

valid, invalid = Registry.build(
    directory=Path(lftw.__file__).parent,
    external_directories=[Path(pyhighlights.__file__).parent],
)
print("invalid:", invalid)


task = Registry.from_key(
    LFTW_GENDER_FR_TASK_TEST2,
    seeds=[42],
    embeddings="classificazione/glove.twitter.27B.25d.txt",
    
    
)

splits = task.splits()
test_only = {"test": splits["test"]}

loaders = task.loaders(test_only) 
model = task.build_model()      

checkpoint_path = "results/lftw_fr_gender/task/2026-10-11T23-55-23/seed=42/epoch=80-step=22437.ckpt"
with th.serialization.safe_globals([RegistrationKey, frozenset, set]):
    state = th.load(checkpoint_path, map_location="cpu")
model.load_state_dict(state["state_dict"])
model.eval()

trainer = L.Trainer(**task.trainer_args)

scores = task.score(
    trainer, model, loaders,
    Path("predictions_test2_gender.pkl"),
)
print(scores)

test_frame = test_only["test"]
examples = {int(row.sample_id): row for row in test_frame.itertuples(index=False)}

batches = pd.read_pickle("predictions_test2_gender.pkl")

def reported_head(masks):
    return masks[:, 0] if masks.ndim == 3 else masks

rows = []
for batch in batches:
    masks = reported_head(np.asarray(batch["highlight_mask"]))
    valid = np.asarray(batch["mask"]) > 0
    predicted = np.asarray(batch["class_logits"])
    if predicted.ndim == 3:
        predicted = reported_head(predicted)
    predicted = predicted.argmax(-1)

    for index, sample_id in enumerate(batch["sample_ids"]):
        example = examples.get(int(sample_id))
        if example is None:
            continue
        tokens = list(example.tokens)
        length = int(valid[index].sum())
        selected = [i for i in np.flatnonzero(masks[index][:length])]
        rows.append({
            "sample_id": int(sample_id),
            "text": example.text,
            "label": int(example.label),
            "predicted": int(predicted[index]),
            "selected_text": " ".join(tokens[i] for i in selected),
            "n_selected": len(selected),
            "n_tokens": length,
        })

results = pd.DataFrame(rows)
print(results.head(20))
print("\nAccuracy:", (results["label"] == results["predicted"]).mean())
results.to_csv("analisi_test2_gender.csv", index=False)

