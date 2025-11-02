from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

# Function to split documents
def split_documents(documents : list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False
    )
    all_splits = text_splitter.split_documents(documents)
    all_splits_with_id = add_unique_ids(all_splits)
    return all_splits_with_id

# Adding unique Ids to each chunk
def add_unique_ids(chunks: list[Document]):
    last_page_id = None
    chunk_number = 0

    for chunk in chunks:
        source = chunk.metadata.get("source") 
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"
        # print(f"Current Page Id {current_page_id}")
        if (current_page_id == last_page_id):
            chunk_number += 1
        else:
            chunk_number = 0
        
        last_page_id = current_page_id
        chunk.metadata["id"] = f"{current_page_id}:{chunk_number}"
        # print(f"Unique Id: {chunk.metadata["id"]}")
    
    return chunks