# Chat with Documents RAG Application

A Retrieval-Augmented Generation (RAG) application built with Streamlit, FastAPI, LangChain, and ChromaDB. Interact with your documents through a conversational interface powered by OpenAI models.

## Features

- **Document Management**: Upload PDF, DOCX, or HTML files and manage them via a sidebar interface.
- **Conversational AI**: Chat with context-aware AI using GPT-4o or GPT-4o-mini models.
- **Session Tracking**: Maintain chat history across sessions with unique session IDs.
- **Vector Search**: Automatically index documents for semantic search using ChromaDB.
- **Logging**: Track user queries, AI responses, and document metadata in a SQLite database.

## Prerequisites

- Python 3.9+
- [OpenAI API Key](https://platform.openai.com/api-keys)
- Required file types for upload: `.pdf`, `.docx`, `.html`

## Installation

1. **Clone the repository**:
   ```bash
   git clone [your-repository-url]
   cd your-repo
2. **Install dependencies:**
   ```
   pip install fastapi streamlit langchain-openai python-dotenv uvicorn sqlite3 pypdf docx2txt unstructured chromadb
   ```
3. **Environment Setup:**
    Create a .env file in the root directory:
   ```
   OPENAI_API_KEY="your-openai-api-key"
   ```

## Configuration

Ensure the chroma_db directory exists for ChromaDB persistence:
```
mkdir chroma_db
```
