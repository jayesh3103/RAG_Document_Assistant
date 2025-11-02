import streamlit as st
from scripts.prompt import prompt_llm
import time

def main_page():
    st.title("RAG Project")
    st.write("Ask a question about your documents.")

    query = st.text_input("Enter Search Query:", key="query_input")

    if query:
        time_placeholder = st.empty()
        start_time = time.time()

        with st.spinner("Thinking..."):
            result = prompt_llm(query)
            
        total_time = time.time() - start_time
        time_placeholder.markdown(f"✅ **Total Time Taken:** {total_time:.2f} seconds")

        st.markdown("---")
        st.markdown("## Response:")
        st.markdown(result)
