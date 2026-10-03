# 📚 PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about multiple PDF documents and receive answers grounded in the retrieved document content.

The system uses semantic retrieval with embeddings, ChromaDB for vector storage, Gemini for answer generation, and displays PDF/page-level source citations in the chatbot UI.

---

## 🚀 Features

- Multi-PDF support
- PDF text extraction
- Page-aware document processing
- Text chunking with overlap
- Semantic embeddings using Sentence Transformers
- ChromaDB vector storage
- Cosine similarity-based retrieval
- Top-K retrieval with distance filtering
- Grounded answer generation using Gemini
- Failure handling for questions outside the indexed documents
- Source and page metadata
- Source/page citations in the UI
- FastAPI backend
- Simple web-based chatbot interface

---

## 🏗️ Architecture

```text
                    PDF Documents
                         │
                         ▼
                  PDF Text Extraction
                         │
                         ▼
                 Chunking + Overlap
                         │
                         ▼
              Sentence Transformer
               (all-MiniLM-L6-v2)
                         │
                         ▼
                  384-D Embeddings
                         │
                         ▼
                     ChromaDB
                         │
                  Semantic Retrieval
                         │
                    Top-K Chunks
                         │
                  Distance Filtering
                         │
                         ▼
                 Context Construction
                         │
                         ▼
                    Gemini LLM
                         │
                         ▼
              Answer + Source Metadata
                         │
                         ▼
                    FastAPI API
                         │
                         ▼
                    Web Frontend
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| PDF Processing | PyMuPDF |
| Embeddings | Sentence Transformers |
| Embedding Model | `all-MiniLM-L6-v2` |
| Vector Database | ChromaDB |
| LLM | Gemini |
| Backend | FastAPI |
| Server | Uvicorn |
| Frontend | HTML, CSS, JavaScript |

---

## 📁 Project Structure

```text
pdf-chatbot/
│
├── backend/
│   ├── api/
│   │   └── main.py
│   │
│   ├── models/
│   │
│   ├── rag/
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── generator.py
│   │   ├── ingest.py
│   │   ├── rag_pipeline.py
│   │   └── vector_store.py
│   │
│   └── services/
│       └── pdf_service.py
│
├── data/
│   ├── uploads/
│   └── chroma_db/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
├── reset_vector_store.py
└── README.md
```

---

## 🔄 How the RAG Pipeline Works

### 1. PDF Extraction

PDF documents are processed page by page using PyMuPDF.

### 2. Chunking

Extracted text is divided into smaller overlapping chunks so that relevant sections can be retrieved independently.

### 3. Embeddings

Each chunk is converted into a numerical vector using:

```text
all-MiniLM-L6-v2
```

The model produces 384-dimensional embeddings.

### 4. Vector Storage

The embeddings are stored persistently in ChromaDB.

```text
Collection: pdf_chunks
Storage: data/chroma_db/
```

Each chunk also stores metadata:

```text
document_id
source
page_number
chunk_index
```

### 5. Question Retrieval

When the user asks a question:

```text
Question
   ↓
Question Embedding
   ↓
ChromaDB Similarity Search
   ↓
Top-K Chunks
   ↓
Distance Filtering
```

### 6. Context Construction

The relevant chunks are combined into a context containing the source PDF and page number.

### 7. Answer Generation

The retrieved context is provided to Gemini, which generates the final answer using the document context.

### 8. Source Citations

The application keeps the source metadata outside the LLM and attaches the retrieved PDF and page information to the final response.

Example:

```text
Sources:
📄 CN.pdf — Page 2
📄 CN.pdf — Page 6
```

---

## 🗄️ Vector Database

The project uses **ChromaDB** as its vector database.

Persistent storage:

```text
data/chroma_db/
```

Collection:

```text
pdf_chunks
```

The collection uses cosine distance for semantic retrieval.

Lower cosine distance indicates greater similarity between the query and retrieved chunk.

---

## 📄 Adding PDF Documents

Place PDF files inside:

```text
data/uploads/
```

For example:

```text
data/uploads/
├── CN.pdf
└── DAA.pdf
```

Then run the ingestion pipeline:

```bash
python -m backend.rag.ingest
```

The ingestion process extracts, chunks, embeds, and stores the documents in ChromaDB.

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Do **not** commit your actual API key to Git.

The `.env` file should be included in `.gitignore`.

---

## ⚙️ Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🌐 Running the Backend

Start the FastAPI server:

```bash
uvicorn backend.api.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 💬 Running the Frontend

Open:

```text
frontend/index.html
```

in a browser while the FastAPI server is running.

The frontend sends questions to:

```text
POST /ask
```

The API returns:

```json
{
  "question": "What is the OSI model?",
  "answer": "The OSI model is...",
  "sources": [
    {
      "source": "CN.pdf",
      "page": 2
    }
  ]
}
```

---

## 🧪 Testing

### Retrieval Test

```bash
python -m backend.test_retrieval
```

### Retrieval Evaluation

```bash
python -m backend.test_retrieval_eval
```

### End-to-End RAG Test

```bash
python -m backend.test_rag
```

### Gemini Test

```bash
python -m backend.test_gemini
```

---

## 🛡️ Grounding and Failure Handling

The system uses retrieval filtering before sending context to Gemini.

If no chunks satisfy the configured retrieval threshold, the system returns:

```text
I could not find the answer in the provided document.
```

This helps prevent the system from answering questions when relevant information cannot be retrieved from the indexed documents.

---

## 📚 Example

### Question

```text
What is the OSI model?
```

### Answer

```text
The OSI (Open Systems Interconnection) model is a conceptual
framework used to understand and standardize the functions of
a telecommunication or computing system. It divides network
communications into seven distinct layers.
```

### Sources

```text
📄 CN.pdf — Page 2
📄 CN.pdf — Page 6
```

---

## ⚠️ Limitations

- Retrieval quality depends on chunking and embedding quality.
- The distance threshold is dataset and embedding-model dependent.
- Very large document collections may require more advanced retrieval strategies.
- Gemini API latency and quota can affect response time.
- The current UI does not directly upload PDFs.
- The current implementation uses a basic similarity retrieval approach without a cross-encoder reranker.

---

## 🔮 Future Improvements

Possible future improvements include:

- Cross-encoder reranking
- Improved chunking strategies
- Streaming responses
- Direct PDF upload from the UI
- Conversation memory
- Authentication
- Retrieval analytics
- Larger automated evaluation datasets
- Production deployment

---

## 📌 Current Project Status

The current implementation includes:

- Multi-PDF RAG
- Semantic retrieval
- Persistent vector storage
- Gemini-based generation
- Grounded responses
- Source/page citations
- FastAPI backend
- Web chatbot interface

The project is currently at the **functional MVP stage**.
