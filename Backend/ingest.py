import uuid

from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL

from vector_store import collection

from loaders.pdf_loader import load_pdf
from loaders.docx_loader import load_docx
from loaders.txt_loader import load_txt
from loaders.faq_loader import load_faq

from processing.chunker import chunk_text

print("INGEST FILE:", __file__)
print("chunk_text:", chunk_text)

model = SentenceTransformer(EMBEDDING_MODEL)


def load_documents():

    documents = []

    documents.extend(

        load_pdf("knowledge")

    )

    documents.extend(

        load_docx("knowledge")

    )

    documents.extend(

        load_txt("knowledge")

    )

    documents.extend(

        load_faq("knowledge/faq.json")

    )

    return documents

def ingest():

    documents = load_documents()

    print("=" * 60)

    print(f"Total Dokumen : {len(documents)}")

    print("=" * 60)

    total_chunks = 0

    for document in documents:

        chunks = chunk_text(

            document["text"]

        )

        print(

            f"{document['source']}"

            f" -> "

            f"{len(chunks)} chunk"

        )

        total_chunks += len(chunks)

        for chunk_index, chunk in enumerate(chunks):

            embedding = model.encode(

                chunk

            ).tolist()

            collection.add(

                ids=[str(uuid.uuid4())],

                embeddings=[embedding],

                documents=[chunk],

                metadatas=[

                    {

                        "source": document["source"],

                        "type": document["type"],

                        "chunk": chunk_index

                    }

                ]

            )

    print("=" * 60)

    print(f"Total Chunk : {total_chunks}")

    print("Embedding selesai dibuat.")

    print("=" * 60)


if __name__ == "__main__":

    ingest()