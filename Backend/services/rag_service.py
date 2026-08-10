from memory import get_history

from models.rag_result import RAGResult

from services.hybrid_retriever import hybrid_search
from services.query_rewriter import rewrite_query
from services.reranker import rerank


class RAGService:

    def retrieve_context(
        self,
        session_id: str,
        question: str
    ) -> RAGResult | None:

        # ==========================
        # Conversation History
        # ==========================

        history = get_history(session_id)

        # ==========================
        # Rewrite Query
        # ==========================

        rewritten_question = rewrite_query(
            history,
            question
        )

        # ==========================
        # Hybrid Search
        # ==========================

        candidates = hybrid_search(
            rewritten_question
        )

        if not candidates:

            return None

        # ==========================
        # Re-ranking
        # ==========================

        ranked = rerank(
            rewritten_question,
            candidates
        )

        # ==========================
        # Build Context
        # ==========================

        context = "\n\n".join(
            item["document"]
            for item in ranked
        )

        sources = [

            item["metadata"]

            for item in ranked

        ]

        return RAGResult(

            question=question,

            rewritten_question=rewritten_question,

            context=context,

            sources=sources,

            documents=ranked

        )


rag_service = RAGService()