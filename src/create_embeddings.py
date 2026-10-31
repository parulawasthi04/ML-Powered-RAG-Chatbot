from chunk_documents import split_documents
from load_pdfs import load_all_pdfs
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

def create_embeddings(chunks):

    embedding_model=HuggingFaceBgeEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    vectors = embedding_model.embed_documents(
        [chunk.page_content for chunk in chunks]
    )

    return vectors


if __name__ == "__main__":

    documents = load_all_pdfs()

    chunks = split_documents(documents)

    vectors = create_embeddings(chunks)

    print("Total chunks:", len(chunks))
    print("Vector dimension:", len(vectors[0]))
