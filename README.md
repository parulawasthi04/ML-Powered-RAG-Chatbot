# 📚 PaperBrain — Advanced Research Paper RAG Assistant

PaperBrain is an **AI-powered research assistant** that answers questions from Machine Learning research papers using an **Advanced Retrieval-Augmented Generation (RAG) pipeline**.

Instead of relying only on a language model’s internal knowledge, the system retrieves relevant sections from research papers and generates **accurate, context-grounded explanations with citations**.

---

# 🚀 Project Overview

Large Language Models can sometimes **hallucinate or provide outdated information** when answering technical questions.

PaperBrain solves this problem using **Retrieval-Augmented Generation (RAG)**.

The system retrieves relevant research paper content and uses it to generate reliable answers.

This ensures:

* ✅ higher factual accuracy
* ✅ research-grounded responses
* ✅ reduced hallucinations
* ✅ transparent citations

---

# 🧠 Advanced RAG Architecture

PaperBrain implements a **multi-stage retrieval pipeline** to improve answer quality.

```
User Query
   │
   ▼
Query Rewriting (LLM)
   │
   ▼
Vector Similarity Search (MMR Retrieval)
   │
   ▼
Document Reranking (Embedding Similarity)
   │
   ▼
Context Compression (LLM Summarization)
   │
   ▼
Prompt Construction
   │
   ▼
Answer Generation (Groq Llama 3.3 70B)
```

This multi-step pipeline ensures the model receives **the most relevant research information before answering**.

---

# ⚙️ System Workflow

## 1️⃣ Load Research Papers

Research papers (PDFs) are loaded from the `data/` directory.

The system processes these documents so they can be searched efficiently.

---

## 2️⃣ Document Chunking

Large research papers are split into smaller chunks.

This improves:

* retrieval accuracy
* embedding quality
* compatibility with LLM context limits

---

## 3️⃣ Embedding Generation

Each chunk is converted into a vector embedding using:

```
sentence-transformers/all-MiniLM-L6-v2
```

Embeddings represent the **semantic meaning of text**.

---

## 4️⃣ Vector Database Storage

All embeddings are stored inside **ChromaDB**.

This enables fast **vector similarity search** to find relevant research paper sections.

---

## 5️⃣ Query Rewriting

User queries are rewritten using an LLM to improve retrieval.

Example:

Original Query

```
What is attention in transformers?
```

Rewritten Query

```
Explain the attention mechanism used in transformer neural networks.
```

This significantly improves **document retrieval accuracy**.

---

## 6️⃣ MMR Retrieval

Documents are retrieved using **Max Marginal Relevance (MMR)**.

MMR balances:

* relevance to the query
* diversity of retrieved documents

This prevents retrieving multiple redundant chunks.

---

## 7️⃣ Document Reranking

Retrieved chunks are reranked using **embedding similarity scoring**.

Steps:

1. Compute embedding for the query
2. Compute embedding for each document
3. Calculate similarity score
4. Sort by relevance

Only the **most relevant research sections** are used.

---

## 8️⃣ Context Compression

Research papers often contain dense technical content.

Each retrieved chunk is summarized into a **compact technical explanation** using the LLM.

Benefits:

* more information fits into context window
* improved reasoning
* cleaner answers

---

## 9️⃣ Answer Generation

The final prompt includes:

* compressed research context
* user question
* structured answer instructions

The system generates a **structured research explanation** containing:

* Definition
* Key Components
* Mathematical Intuition
* Advantages
* Limitations

---

# 🖥 Streamlit Interface

The project includes a **Streamlit chat interface** that provides:

* ChatGPT-style UI
* Real-time question answering
* AI thinking animation
* Research assistant style interaction

Users can simply **ask questions about research papers**.

---

# 📂 Project Structure

```
PaperBrain
│
├── data/
│   └── Research paper PDFs
│
├── db/
│   └── Chroma vector database
│
├── src/
│   ├── load_pdfs.py
│   ├── chunk_documents.py
│   ├── create_embeddings.py
│   ├── store_in_chroma.py
│   └── retrieve_chunks.py
│
├── app.py
├── paper_brain.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🧰 Tech Stack

### Programming Language

Python

### LLM Inference

Groq API

Model Used:

```
llama-3.3-70b-versatile
```

### Frameworks

LangChain

### Embeddings

Sentence Transformers

### Vector Database

ChromaDB

### Frontend

Streamlit

---

# 🔑 Environment Setup

Create a `.env` file in the root directory.

```
GROQ_API_KEY=your_groq_api_key
```

This key allows access to the **Groq LLM inference API**.

---

# ⚙️ Installation

### Clone the repository

```
git clone https://github.com/yourusername/ML-Powered-RAG-Chatbot.git
```

### Move into the project directory

```
cd ML-Powered-RAG-Chatbot
```

### Create virtual environment

```
python -m venv venv
```

### Activate virtual environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run the Streamlit interface:

```
streamlit run app.py
```

The system will open a browser interface where users can **ask questions about research papers**.

---

# 📊 Example Query

```
What is the attention mechanism in transformer models?
```

Example Output:

Definition
Explanation of attention mechanism used in transformers.

Key Components

* Query
* Key
* Value

Mathematical Intuition
Explanation of attention score computation.

Advantages

* Captures long-range dependencies
* Enables parallel computation

Limitations

* Computationally expensive for long sequences

Citations

* Source research papers used for generating the answer

---

# 🎯 Key Features

* Advanced Retrieval-Augmented Generation pipeline
* Query rewriting for better retrieval
* Max Marginal Relevance document search
* Embedding-based document reranking
* Context compression using LLM summarization
* Research paper grounded answers
* Automatic citation extraction
* Interactive Streamlit chat interface

---

# 🔍 Why Use RAG?

Traditional language models rely only on training data.

RAG improves performance by retrieving **external knowledge at query time**.

Benefits include:

* reduced hallucinations
* more factual answers
* transparent citations
* up-to-date research knowledge

---

# 📈 Future Improvements

Possible future enhancements:

* Hybrid search (BM25 + vector search)
* Cross-encoder reranking
* Multi-document reasoning
* Retrieval evaluation metrics
* Automatic citation highlighting
* Agentic RAG workflows

---

# 👨‍💻 Author

Parul Awasthi

Master in Computer Applications
National Institute of Technology Raipur

### Interests

Machine Learning
Data Science
AI Systems
Retrieval Augmented Generation
LLM Applications
=======
# ML-Powered-RAG-Chatbot
