from ollama import chat

from config import MODEL_NAME

from memory import (
    add_message,
    get_history
)

from services.rag_service import rag_service

from services.prompt_builder import (
    build_messages
)


def get_response(session_id, message):
    """
    Menghasilkan jawaban chatbot menggunakan pipeline RAG.

    Workflow:
    User Question
            │
            ▼
      Hybrid Retrieval
            │
            ▼
      Prompt Builder
            │
            ▼
         Ollama LLM
            │
            ▼
      Simpan Memory
            │
            ▼
        Return Reply
    """

    # ==========================
    # Retrieve Context
    # ==========================

    retrieval = rag_service.retrieve_context(
        session_id,
        message
    )

    if retrieval is None:
        return (
            "Maaf, informasi tersebut belum tersedia "
            "di basis pengetahuan perusahaan."
        )

    # ==========================
    # Conversation History
    # ==========================

    history = get_history(session_id)

    # ==========================
    # Build Prompt
    # ==========================

    messages = build_messages(
        history,
        retrieval.context,
        message
    )

    # ==========================
    # Generate Response
    # ==========================

    response = chat(
        model=MODEL_NAME,
        messages=messages
    )

    reply = response["message"]["content"].strip()

    # ==========================
    # Save Memory
    # ==========================

    add_message(
        session_id,
        "user",
        message
    )

    add_message(
        session_id,
        "assistant",
        reply
    )

    # ==========================
    # Return
    # ==========================

    return reply