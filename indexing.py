from collections import defaultdict

# مرحله 2: ساخت ایندکس معکوس
def build_inverted_index(processed_docs):
    inverted_index = defaultdict(list)

    for doc_id, tokens in enumerate(processed_docs):
        for token in tokens:
            if doc_id not in inverted_index[token]:
                inverted_index[token].append(doc_id)

    return inverted_index
