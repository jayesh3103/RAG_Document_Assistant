import os
from langchain_community.document_loaders import PyPDFLoader

# Functin to load all the documents from a directory
def load_documents(directory_path: str):
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(directory_path, filename))
            docs = loader.load()
            documents.extend(docs)
    return documents

load_documents("data")
