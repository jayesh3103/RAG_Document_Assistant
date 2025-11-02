import streamlit as st
from ui.sidebar import show_documents
from ui.main_page import main_page

# Function to load/split and upload data to vector store
# Needs to be run only once, or when new data is added
# from scripts.populate import populate_db
# populate_db()

st.set_page_config(page_title="RAG Project", page_icon="🤖", layout="wide")

show_documents()
main_page()