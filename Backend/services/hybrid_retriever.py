from services.retriever_service import retriever_service
from services.bm25_service import bm25_service

from config import TOP_K


def hybrid_search(query):

    semantic = retriever_service.semantic_search(
        query,
        TOP_K
    )

    keyword = bm25_service.search(
        query,
        TOP_K
    )

    merged = {}

    # ===========================
    # Semantic Search
    # ===========================

    for item in semantic:

        metadata = item["metadata"]

        key = (
            metadata.get("source", "unknown"),
            metadata.get("chunk", 0)
        )

        item["semantic_score"] = 1 - item["distance"]

        merged[key] = item

    # ===========================
    # BM25 Search
    # ===========================

    for item in keyword:

        metadata = item["metadata"]

        key = (
            metadata.get("source", "unknown"),
            metadata.get("chunk", 0)
        )

        if key in merged:

            merged[key]["bm25_score"] = item["bm25_score"]

        else:

            item["semantic_score"] = 0

            merged[key] = item

    return list(merged.values())