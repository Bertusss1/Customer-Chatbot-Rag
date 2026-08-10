from ollama import chat

from config import MODEL_NAME


def rewrite_query(history, question):

    if not history:
        return question

    messages = [

        {
            "role": "system",
            "content":
            """
Ubah pertanyaan lanjutan menjadi pertanyaan lengkap.

Jangan menjawab pertanyaan.

Hanya keluarkan pertanyaan baru.
            """
        }

    ]

    messages.extend(history[-6:])

    messages.append({

        "role": "user",

        "content": question

    })

    response = chat(

        model=MODEL_NAME,

        messages=messages

    )

    return response["message"]["content"].strip()