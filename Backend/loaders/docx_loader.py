from pathlib import Path
from docx import Document


def load_docx(folder):

    documents = []

    for file in Path(folder).glob("*.docx"):

        doc = Document(file)

        text = "\n".join(

            paragraph.text

            for paragraph in doc.paragraphs

            if paragraph.text.strip()

        )

        documents.append({

            "source": file.name,

            "type": "docx",

            "text": text

        })

    return documents