# 🧠 RAG Portfolio Bot

A production-structured Retrieval-Augmented Generation (RAG) system that answers questions using custom documents.

This project demonstrates:

* Modular RAG architecture
* Persistent vector storage (Chroma)
* Conversational query rewriting (coreference resolution)
* Clean separation of ingestion, retrieval, and generation layers
* Production-ready folder structure

---

## 🚀 Features

* 📄 Document ingestion pipeline
* ✂️ Smart chunking with overlap
* 🔎 Semantic search using vector embeddings
* 🧠 Conversational query rewriting
* 🤖 LLM-based grounded answer generation
* 💾 Persistent Chroma vector database

---

## 🏗 Architecture Overview

```
User Question
   ↓
Query Rewriter (Coreference Resolution)
   ↓
Vector Retrieval (Chroma)
   ↓
Context Injection
   ↓
LLM Generates Grounded Answer
```

---

## 🛠 Tech Stack

* LangChain
* Chroma (Persistent Vector DB)
* Ollama / OpenAI (LLM)
* Python 3.10+

---

## ⚙️ Setup

### 1️⃣ Clone Repo

```bash
git clone https://github.com/gritik418/rag-portfolio-bot.git
cd rag-portfolio-bot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Documents

Place your `.txt` files inside:

```
docs/
```

---

## 📥 Run Ingestion

This builds and persists the vector database.

```bash
python -m app.ingestion.ingest
```

You should see:

```
Starting ingestion pipeline...
Vectorstore created.
```

---

## 💬 Run Chat Interface

```bash
python -m app.main
```

Ask questions like:

```
What projects has Ritik worked on?
Tell me more about it.
```

The system will:

* Rewrite follow-up queries
* Retrieve relevant chunks
* Generate grounded answers
