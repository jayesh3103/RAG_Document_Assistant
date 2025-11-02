from langchain_chroma import Chroma
from scripts.embeder import get_embedding_function

def search_db(query: str, k: int | None = 2):
    vector_store = Chroma(
        collection_name="aws",
        embedding_function=get_embedding_function(),
        persist_directory="./chroma_langchain_db"
    )

    results = vector_store.similarity_search(query, k=k)
    return results