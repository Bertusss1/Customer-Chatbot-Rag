from models.rag_result import RAGResult


def format_sources(
    result: RAGResult
):

    if not result.sources:

        return ""

    text = "\n\n### Sumber\n"

    seen = set()

    for source in result.sources:

        key = (

            source["source"],

            source["chunk"]

        )

        if key in seen:

            continue

        seen.add(key)

        text += (
            f"- {source['source']} "
            f"(Chunk {source['chunk']})\n"
        )

    return text