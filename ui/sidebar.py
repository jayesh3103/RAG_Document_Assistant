import streamlit as st
import os

def get_file_icon(file_name):
    if file_name.endswith(".pdf"):
        return "📄"
    elif file_name.endswith(".txt"):
        return "📝"
    else:
        return "📁"

def show_documents():
    st.sidebar.title("Documents")
    data_dir = "data"
    if os.path.exists(data_dir):
        files = os.listdir(data_dir)
        if not files:
            st.sidebar.write("No documents found.")
        else:
            for file in files:
                icon = get_file_icon(file)
                st.sidebar.markdown(f"- {icon} {file}")
    else:
        st.sidebar.write("`data` directory not found.")
