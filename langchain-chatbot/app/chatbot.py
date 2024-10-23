from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

class Chatbot:
    def __init__(self):
        # Load the vector store
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

        # Create a retrieval-based QA chain
        llm = OpenAI()
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever()
        )

    def get_response(self, query):
        return self.qa_chain.run(query)
