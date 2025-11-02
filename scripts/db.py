from langchain.schema.document import Document
from langchain_chroma import Chroma
from scripts.embeder import get_embedding_function

# Function to add chunks to chroma
def add_to_chroma(chunks: list[Document]):
    vector_store = Chroma(
        collection_name="aws",
        embedding_function=get_embedding_function(),
        persist_directory="./chroma_langchain_db"
    )

    existing_items = vector_store.get()
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in the database: {len(existing_ids)}")


    # Only add documents that don't exist in the db
    new_chunks = []
    for chunk in chunks:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)
    ids = None   
    if len(new_chunks):
        print(f"Adding {len(new_chunks)} documents to the vector store.")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        ids = vector_store.add_documents(new_chunks, ids=new_chunk_ids)
    else:
        print("No new documents to add.")
    
    return ids
