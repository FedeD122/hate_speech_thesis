import re

# trasformo gli highlights

TARGET_CATS = ["Ethnicity", "Gender", "Religion", "Sexual Orientation"]
CHARS = "'’‘`\u0018\u0019\"“”"



def build_fuzzy_pattern(s: str) -> str:
    parts, prev_was_space = [], False
    for ch in s:
        if ch.isspace():
            if not prev_was_space:
                parts.append(f"[\\s{re.escape(CHARS)}]+")
            prev_was_space = True
            continue
        prev_was_space = False
        if ch in CHARS:
            parts.append(f"[{re.escape(CHARS)}]")
        else:
            parts.append(re.escape(ch))
    return "".join(parts)


def find_span(text: str, prediction: str):
    prediction = prediction.strip()
    if not prediction:
        return None
    m = re.search(build_fuzzy_pattern(prediction), text, re.IGNORECASE | re.DOTALL)
    return (m.start(), m.end()) if m else None


def tokenize_with_offsets(text: str):
    """Stessi confini di str.split(), ma con l'offset di ogni token nel testo."""
    return [(m.group(), m.start(), m.end()) for m in re.finditer(r"\S+", text)]


def build_highlight_vector(text: str, row, categories: list = None) -> list:
    """Unione delle categorie indicate: 1 se il token cade in almeno uno span estratto."""
    cats = categories if categories is not None else TARGET_CATS

    token_spans = tokenize_with_offsets(text)
    vector = [0] * len(token_spans)
    for cat in cats:
        val = row.get(cat, "absent")
        if not isinstance(val, str) or val.strip().lower() == "absent":
            continue
        span = find_span(text, val)
        if span is None:
            continue
        start, end = span
        for i, (_, t_start, t_end) in enumerate(token_spans):
            if t_start < end and t_end > start:
                vector[i] = 1
    return vector

def clean_and_union_spans(spans_list):
    valid_spans = set()
    for s in spans_list:
        if isinstance(s, str) and s.strip().lower() != "absent":
            valid_spans.add(s)
    if not valid_spans:
        return "absent"
        
    sorted_spans = sorted(list(valid_spans), key=len, reverse=True)
    filtered = []
    for span in sorted_spans:
        if not any(span in longer_span for longer_span in filtered):
            filtered.append(span)
            
    return " , ".join(filtered) if filtered else "absent"
