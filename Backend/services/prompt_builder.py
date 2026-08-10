SYSTEM_PROMPT = """
# ROLE

Anda adalah AI Customer Service perusahaan.

# TUJUAN

Berikan jawaban yang akurat berdasarkan knowledge base perusahaan.

# ATURAN

1. Gunakan HANYA informasi pada KNOWLEDGE.
2. Jangan menambah informasi baru.
3. Jangan membuat asumsi.
4. Jika informasi tidak ditemukan, katakan:

"Maaf, informasi tersebut belum tersedia di basis pengetahuan perusahaan."

5. Jawab dalam Bahasa Indonesia.
6. Maksimal 5 kalimat.
"""


def build_messages(history, context, question):

    prompt = f"""
# KNOWLEDGE

{context}

# QUESTION

{question}

# ANSWER
"""

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

    ]

    messages.extend(history)

    messages.append({

        "role": "user",

        "content": prompt

    })

    return messages