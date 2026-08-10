from dataclasses import dataclass
from typing import Any


@dataclass
class RAGResult:
    """
    Hasil akhir pipeline RAG.
    """

    question: str

    rewritten_question: str

    context: str

    sources: list[dict]

    documents: list[dict[str, Any]]