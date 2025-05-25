
# Modular LangChain Chat App with Streamlit

This project is a **modular AI assistant web application** using **Streamlit** for the frontend and **LangChain** for orchestration. It enables chat-driven experiences and backend utility calls via OpenAI, with clearly separated logic for queries, API integrations, models, and LangChain chains.

---

## Key Features

- Chat with AI using LangChain agents
- Clean modular code structure
- Plug-in architecture for tools and APIs
- Streamlit interface for user interaction
- Secure API key handling with `.env`

---

## Project Structure

```

.
├── streamlit\_app.py       # Streamlit UI entrypoint
├── query.py               # Chat query handler
├── langchain\_utils.py     # Chains, prompts, LangChain tools
├── api\_utils.py           # Custom API integrations
├── pydantic\_models.py     # Typed input/output using Pydantic
├── requirements.txt       # Project dependencies
├── .env                   # Secret environment variables

````

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/langchain-chat-modular.git
cd langchain-chat-modular
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with the following format:

```
OPENAI_API_KEY=your_openai_api_key_here
OTHER_API_KEY=if_applicable
```

> Add any additional API keys required by `api_utils.py`.

---

## How It Works

* `streamlit_app.py`: Renders the chat UI, handles user inputs and displays AI responses.
* `query.py`: Manages user queries and interacts with LangChain agents/tools.
* `langchain_utils.py`: Defines chains, prompts, and custom LangChain components.
* `api_utils.py`: Includes external API logic (e.g., weather, search, finance).
* `pydantic_models.py`: Provides strict schemas for inputs and outputs.

---

## Running the App

```bash
streamlit run streamlit_app.py
```

---

## Built With

* [Streamlit](https://streamlit.io/)
* [LangChain](https://www.langchain.com/)
* [OpenAI](https://openai.com/)
* [Pydantic](https://docs.pydantic.dev/)
* [Requests](https://docs.python-requests.org/)

---

## Extensibility

You can easily extend this app by:

* Adding new tools to `langchain_utils.py`
* Creating APIs in `api_utils.py`
* Defining new schemas in `pydantic_models.py`
* Updating the UI or input controls in `streamlit_app.py`

---

## Deployment

Supports deployment to:

* Streamlit Community Cloud
* Docker (add `Dockerfile`)

Make sure to configure secrets in deployment environments.

---

## TODO / Improvements

* [ ] Add multi-turn memory
* [ ] Implement error logging and tracing
* [ ] Add support for multiple agents
* [ ] Include user authentication for session-based chat

---

## License

MIT License

