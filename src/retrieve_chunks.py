from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma

DB_PATH="db"

def retrieve_similar_chunks(query):

    print("Loading embedding model")

    embedding_model=HuggingFaceBgeEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Loading vector database....")
    db=Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model
    )
    print("Search for the user query in similar chunks...")
    results=db.similarity_search(query,k=3)

    return results


if __name__=='__main__':

    while True:
        query = input("\nAsk something about your ML papers: ")

        results = retrieve_similar_chunks(query)

        print("\nTop 3 Relevant Chunks:\n")

        for i, doc in enumerate(results):
            print(f"\n--- Result {i+1} ---")
            print(doc.page_content[:500])

