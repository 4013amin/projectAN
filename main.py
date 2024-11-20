from preprocessing import preprocess_text
from indexing import build_inverted_index

# نمونه متون
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# پیش‌پردازش متون
processed_docs = [preprocess_text(doc) for doc in documents]

# ساخت ایندکس معکوس
inverted_index = build_inverted_index(processed_docs)

print("Inverted Index:", inverted_index)
