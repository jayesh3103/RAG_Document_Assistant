from langchain_ollama import OllamaEmbeddings

# Function to return embedding function
def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text:v1.5")
    return embeddings