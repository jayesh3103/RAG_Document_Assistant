from scripts.query import search_db
from ollama import generate

# Function to generate prompt
def generate_prompt(query: str):
    print("Searching for relevant docs in the Vector Store...")
    # Search for relevant documents in the Vector Database
    relevant_docs = search_db(query, 10)

    formatted_docs = []
    for i, doc in enumerate(relevant_docs):
        text = doc.page_content
        src = doc.metadata["id"]
        lines = f"Source Id: {src}\n{text}\n<-------------END----------->\n"
        formatted_docs.append(lines)

    context = "\n\n".join(formatted_docs)

    PROMPT = f"""
    You are an expert AI assistant specialized in answering questions factually using only the given context.

    ### CONTEXT
    {context}

    ---

    ### TASK
    Answer the user question below *strictly using the provided context*. 
    If the context does not contain enough information, explicitly state:
    "Insufficient information in the provided context to fully answer the question."

    ### INSTRUCTIONS
    1. Provide a clear, structured, and pointwise answer. Use numbered or bulleted points where possible.
    2. For comparison or differentiation questions, include a clean and concise **markdown table**.
    3. Maintain an objective, factual tone — do **not** speculate or include outside knowledge.
    4. Reference every statement to the relevant source chunk(s) at the end in the format:
    **Sources:** [Chunk-IDs or filenames you used].
    5. If multiple parts of context contribute to the same point, cite all of them.

    ---

    ### QUESTION
    {query}

    Now produce the best possible answer:
    """
    return PROMPT


# Function to prompt local llm 
def prompt_llm(query: str, model: str | None = "llama3.2:3b"):
    print("Generating Augmented Prompt...")
    prompt = generate_prompt(query)
    # print(f"Prompt :\n {prompt}\n")
    print("Generating Response...")
    response = generate(
        model=model,
        prompt=prompt
    )
    return response.response

