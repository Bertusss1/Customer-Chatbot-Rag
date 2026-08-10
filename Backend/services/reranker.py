from sentence_transformers import CrossEncoder

from config import (
    RERANK_MODEL,
    FINAL_TOP_K
)

model = CrossEncoder(RERANK_MODEL)


def rerank(query, documents):

    if not documents:
        return []

    pairs = []

    for item in documents:

        pairs.append(

            (
                query,
                item["document"]
            )

        )

    scores = model.predict(pairs)

    ranked = []

    for score, item in zip(scores, documents):

        item["score"] = float(score)

        ranked.append(item)

    ranked.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return ranked[:FINAL_TOP_K]