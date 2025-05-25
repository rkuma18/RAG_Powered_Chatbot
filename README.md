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

## Running the Application

1. Start the FastAPI backend:
   ```
   uvicorn main:app --reload
   ```
   The API will run at http://localhost:8000.

2. Launch the Streamlit frontend (in a separate terminal):
   ```
   streamlit run streamlit_app.py
   ```
   Access the UI at http://localhost:8501.

## Usage
1. Upload Documents:
  * Use the sidebar to upload supported files.
  * Documents are automatically indexed and stored in ChromaDB.
2. Chat Interface:
   * Select a model (GPT-4o or GPT-4o-mini) from the sidebar.
   * Type queries in the chat input to interact with your documents.
   * View detailed responses under the "Details" expander.
3. Manage Documents:
   * Refresh the document list or delete files via the sidebar.
   * Deletions remove both database records and ChromaDB embeddings.

## API Endpoints
|- Endpoint |	Method |	Description|
|---|---|---|
|- /chat| 	POST |	Process user queries|
|- /upload-doc |	POST |	Upload and index documents|
|- /list-docs |	GET |	List uploaded documents|
|- /delete-doc |	POST |	Delete a document|

## Project Structure
.
├── streamlit_app.py          # Main Streamlit frontend
├── main.py                   # FastAPI backend
├── sidebar.py                # Streamlit document management UI
├── chat_interface.py         # Streamlit chat UI
├── api_utils.py              # API client functions
├── pydantic_models.py        # Data validation models
├── langchain_utils.py        # RAG chain setup
├── chroma_utils.py           # ChromaDB document indexing
├── db_utils.py               # SQLite database operations
└── .env                      # Environment variables
