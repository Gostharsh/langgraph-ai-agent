from rag.config import reranker
from rag.query.query_expander import QueryExpander

class Retriever:

    def __init__(self, store):
        self.store = store
        self.expander = QueryExpander()

    def retrieve(
        self,
        question
    ):

        # results = self.store.search(question)

        queries = self.expander.expand(question)
        print("\nQUERIES:")
        print(queries)

        

        for query in queries:
            results = self.store.search(query)

            print("\nQUERY:", query)



        filtered_docs = []
        filtered_metas = []

        print("\n===== RETRIEVAL DEBUG =====")

        for doc, meta, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):
            print("\nDistance:", distance)
            print("Source:", meta["source"])
            print("Page:", meta["page"])
            print(doc[:200])

            #distance filtering(0.9)

            if distance < 1.1:
                filtered_docs.append(doc)
                filtered_metas.append(meta)

        # fallback
        if not filtered_docs:
            filtered_docs = results["documents"][0][:3]
            filtered_metas = results["metadatas"][0][:3]

        print("\n===========================")

        return self.rerank(
            question,
            filtered_docs,
            filtered_metas
        )



    def rerank(
        self,
        question,
        docs,
        metas
    ):

        pairs = [
            (question, doc)
            for doc in docs
        ]

        scores = reranker.predict(pairs)

        ranked = sorted(
            zip(docs, metas, scores),
            key=lambda x: x[2],
            reverse=True
        )

        print("\n===== RERANKING =====")

        for doc, meta, score in ranked:
            print(
                f"{score:.4f} | "
                f"{meta['source']} | "
                f"Page {meta['page']}"
            )

            print(doc[:150])
            print("-" * 50)

        print("=====================\n")

        best_docs = [
            item[0]
            for item in ranked[:5]
        ]

        best_metas = [
            item[1]
            for item in ranked[:5]
        ]

        return best_docs, best_metas