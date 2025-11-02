from scripts.loader import load_documents
from scripts.splitter import split_documents
from scripts.db import add_to_chroma

def populate_db():
    data_directory = "data"

    # Loading documents
    documents = load_documents(data_directory)
    print(f"Documents Size: {len(documents)}")
    print("Loaded all documents.")

    # Splitting Documents
    chunks = split_documents(documents)
    print(f"Chunks Size: {len(chunks)}")
    print("Chunked all the documents.")

    # Adding chunks to chroma
    ids = add_to_chroma(chunks)
    if id is not None:
        print(f"Ids Count: {len(ids)}")
        for id in ids:
            print(id)
        print("Added chunks to the chroma db.")