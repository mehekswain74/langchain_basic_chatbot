from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

def extract_and_store_data():
    # Load data from the URL
    loader = WebBaseLoader("https://brainlox.com/courses/category/technical")
    data = loader.load()

    # Split the text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(data)

    # Create embeddings and store in FAISS
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)

    # Save the vector store
    vector_store.save_local("faiss_index")

if __name__ == "__main__":
    extract_and_store_data()
