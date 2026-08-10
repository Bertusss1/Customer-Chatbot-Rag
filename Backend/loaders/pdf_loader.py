from pathlib import Path
from pypdf import PdfReader


def load_pdf(folder):

    documents = []

    for file in Path(folder).glob("*.pdf"):

        reader = PdfReader(file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        documents.append({

            "source": file.name,

            "type": "pdf",

            "text": text.strip()

        })

    return documents