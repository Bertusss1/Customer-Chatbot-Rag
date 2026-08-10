import json


def load_faq(path):

    documents = []

    with open(path, "r", encoding="utf-8") as file:

        faq = json.load(file)

    for item in faq:

        documents.append({

            "source": "faq.json",

            "type": "faq",

            "text": (
                f"Pertanyaan:\n"
                f"{item['question']}\n\n"
                f"Jawaban:\n"
                f"{item['answer']}"
            )

        })

    return documents