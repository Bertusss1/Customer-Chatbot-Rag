import chromadb

from config import DB_PATH, COLLECTION_NAME

client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

def get_all_documents():

    data = collection.get(

        include=[
            "documents",
            "metadatas"
        ]
    )

    results = []

    for doc, meta in zip(

        data["documents"],

        data["metadatas"]

    ):

        results.append({

            "document": doc,

            "metadata": meta

        })

    return results