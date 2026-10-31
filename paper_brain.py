import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()

DB_PATH = "db"


# -----------------------------
# Load Embeddings
# -----------------------------
def load_embeddings():
    return HuggingFaceBgeEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# -----------------------------
# Load Vector Database
# -----------------------------
def load_vector_db():
    embeddings = load_embeddings()

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )


# -----------------------------
# Load Groq LLM
# -----------------------------
def load_llm():
    return ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2
    )

# -----------------------------
# Query Rewriting
# -----------------------------
def rewrite_query(query, llm):

    prompt = f"""
Rewrite the user question to improve retrieval from research papers.

Original Question:
{query}

Rewritten Question:
"""

    response = llm.invoke(prompt)

    return response.content.strip()


# -----------------------------
# MMR Retrieval
# -----------------------------
def retrieve_documents(query, db):

    docs = db.max_marginal_relevance_search(
        query,
        k=6,
        fetch_k=20
    )

    return docs


# -----------------------------
# Reranking
# -----------------------------
def rerank_documents(query, docs, embeddings):

    query_embedding = embeddings.embed_query(query)

    scored_docs = []

    for doc in docs:

        doc_embedding = embeddings.embed_query(doc.page_content)

        score = sum(a*b for a, b in zip(query_embedding, doc_embedding))

        scored_docs.append((score, doc))

    scored_docs.sort(reverse=True, key=lambda x: x[0])

    return [doc for _, doc in scored_docs[:4]]


# -----------------------------
# Context Compression
# -----------------------------
def compress_context(docs, llm):

    summaries = []

    for doc in docs:

        prompt = f"""
Summarize the following research text in a concise technical way.

Text:
{doc.page_content}

Summary:
"""

        response = llm.invoke(prompt)

        summaries.append(response.content)

    return summaries


# -----------------------------
# Main RAG Pipeline
# -----------------------------
def generate_answer(query):

    db = load_vector_db()

    llm = load_llm()

    embeddings = load_embeddings()

    print("\n---- STEP 1: QUERY REWRITE ----")

    new_query = rewrite_query(query, llm)

    print("Rewritten Query:", new_query)

    print("\n---- STEP 2: MMR RETRIEVAL ----")

    docs = retrieve_documents(new_query, db)

    print("Retrieved documents:", len(docs))

    print("\n---- STEP 3: RERANKING ----")

    docs = rerank_documents(query, docs, embeddings)

    print("Top documents:", len(docs))

    print("\n---- STEP 4: CONTEXT COMPRESSION ----")

    summaries = compress_context(docs, llm)

    papers = set()

    for doc in docs:
        if "source" in doc.metadata:
            papers.add(doc.metadata["source"])

    context = "\n\n".join(summaries)

    prompt = f"""
You are an expert Machine Learning research assistant.

Your task is to carefully read the research paper context and provide a clear,
well-structured explanation of the concept asked in the question.

Important guidelines:
- Use ONLY the provided research paper context
- Do NOT copy sentences directly from the context
- Explain ideas in your own words
- Write detailed and meaningful explanations
- Use academic but easy-to-understand language

Structure your answer as follows:

Definition:
Write a clear paragraph explaining the concept and its purpose.

Key Components:
Explain the important components of the method or idea in a detailed paragraph.

Mathematical Intuition:
Explain the underlying mathematical idea or intuition behind the concept.

Advantages:
Describe why this approach is useful in machine learning or research.

Limitations:
Explain potential challenges or limitations of the approach.

Research Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    answer = response.content

    if papers:

        answer += "\n\n📚 Citations:\n"

        for paper in papers:
            answer += f"- {paper}\n"

    return answer


# -----------------------------
# CLI Interface
# -----------------------------
if __name__ == "__main__":

    print("\n📚 Paper Brain Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("Ask a research question: ")

        if query.lower() == "exit":
            break

        answer = generate_answer(query)

        print("\n==============================")
        print("ANSWER")
        print("==============================\n")

        print(answer)