from sentence_transformers import SentenceTransformer

from config import (
    EMBEDDING_MODEL,
    SIMILARITY_THRESHOLD
)

from vector_store import collection


class RetrieverService:

    def __init__(self):

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def semantic_search(
        self,
        query,
        top_k=10
    ):

        embedding = self.model.encode(
            query
        ).tolist()

        results = collection.query(

            query_embeddings=[embedding],

            n_results=top_k,

            include=[

                "documents",

                "metadatas",

                "distances"

            ]

        )

        retrieved = []

        documents = results["documents"][0]

        metadatas = results["metadatas"][0]

        distances = results["distances"][0]

        for doc, meta, distance in zip(

            documents,

            metadatas,

            distances

        ):

            if distance > SIMILARITY_THRESHOLD:

                continue

            retrieved.append({

                "document": doc,

                "metadata": meta,

                "distance": distance

            })

        return retrieved


retriever_service = RetrieverService()