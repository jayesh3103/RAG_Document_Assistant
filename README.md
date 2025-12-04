# RAG Document Assistant

This project implements a Retrieval-Augmented Generation (RAG) pipeline using Python, LangChain, and Streamlit. It allows users to chat with their documents by leveraging a local Large Language Model (LLM) and a vector store for efficient information retrieval.

## Project Overview

The application performs the following steps:

1.  Loads documents from a specified directory (`data/`).
2.  Splits the documents into smaller chunks.
3.  Generates embeddings for each chunk using a local embedding model (`nomic-embed-text`).
4.  Stores the chunks and their embeddings in a ChromaDB vector store.
5.  Provides a Streamlit-based web interface for users to ask questions.
6.  Retrieves relevant document chunks from the vector store based on the user's query.
7.  Uses a local LLM (`llama3.2:3b`) via Ollama to generate a response based on the retrieved context.

## Installation

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.in/jayesh3103/RAG_Document_Assistant.git
cd rag-langchain
```

### 2. Create a Python Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

### 4. Install and Configure Ollama

This project uses [Ollama](https://ollama.com) to serve the LLM and embedding models locally.

1.  Download and install Ollama from the official website.
2.  Pull the required models by running the following commands in your terminal:
    ```bash
    ollama pull llama3.2:3b
    ```
    ```bash
    ollama pull nomic-embed-text:v1.5
    ```

## How to Run

### 1. Populate the Vector Database

Before running the application for the first time, you need to process your documents and populate the ChromaDB vector store.

1.  Place your documents (e.g., `.pdf` files) inside the `data/` directory.
2.  In the `app.py` file, uncomment the line `populate_db()`.
    ```python
    # from scripts.populate import populate_db
    # populate_db() # <- Uncomment this line
    ```
3.  Run the Streamlit app once to execute the population script:
    ```bash
    streamlit run app.py
    ```
4.  Once the database is populated (you'll see files appear in the `chroma_langchain_db` directory), stop the app and **comment out** the `populate_db()` line in `app.py` again to prevent it from running every time.

### 2. Run the Streamlit Application

After populating the database, you can run the main application.

```bash
streamlit run app.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## Demo & Testing

- For a visual walkthrough of the application, check out the demo video located at `assets/rag-langchain-video.mp4`.
- To see a few sample test cases, questions, and their expected outcomes, please refer to the `TESTING.md` file.
