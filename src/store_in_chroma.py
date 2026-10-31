from load_pdfs import load_all_pdfs
from chunk_documents import split_documents
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma

DB_PATH="db"

def store_embeddings():

    print("Loading documents wait yrr.....")
    documents=load_all_pdfs()

    print("lets split it like fruit ninja (into chunks)...")
    chunks=split_documents(documents)

    print("Create embeddings model....")
    embedding_model=HuggingFaceBgeEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    print("Storing in Chroma DB...")

    db = Chroma.from_documents(
        chunks,
        embedding_model,
        persist_directory=DB_PATH
    )

    db.persist()

    print("Done! Dhruv Ml paper Vector database created.")


if __name__ == "__main__":
    store_embeddings()