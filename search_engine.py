from collections import defaultdict

def build_index(docs):
    index = defaultdict(set)

    for i, text in enumerate(docs):
        doc_id = f"doc{i+1}"
        words = text.split()

        for word in words:
            index[word].add(doc_id)

    return index


def search(query, index):
    words = query.split()

    doc_sets = []
    freq = defaultdict(int)

    for w in words:
        if w in index:
            docs = index[w]
            doc_sets.append(docs)

            for d in docs:
                freq[d] += 1  

    if not doc_sets:
        return []

    intersection = set.intersection(*doc_sets)

    union = set.union(*doc_sets)

    ranked = sorted(union, key=lambda d: freq[d], reverse=True)

    return ranked