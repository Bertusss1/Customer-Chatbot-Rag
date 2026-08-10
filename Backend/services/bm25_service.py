from rank_bm25 import BM25Okapi

from processing.preprocess import tokenize


class BM25Service:

    def __init__(self):

        self.documents = []

        self.bm25 = None

    def build(self, documents):

        self.documents = documents

        corpus = [
            tokenize(doc["document"])
            for doc in documents
        ]

        self.bm25 = BM25Okapi(corpus)

        print(f"BM25 indexed {len(documents)} documents.")

    def search(self, query, top_k=10):

        if self.bm25 is None:

            return []

        scores = self.bm25.get_scores(
            tokenize(query)
        )

        ranking = sorted(

            zip(scores, self.documents),

            key=lambda x: x[0],

            reverse=True

        )

        results = []

        for score, item in ranking[:top_k]:

            result = item.copy()

            result["bm25_score"] = float(score)

            results.append(result)

        return results


bm25_service = BM25Service()