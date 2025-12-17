# DevDocs AI: An Intelligent Q&A Bot for Technical Documentation

## 🎯 The Problem

Developers spend a significant amount of time manually searching through dense and complex technical documentation. This is a major bottleneck that breaks concentration and slows down the development process. DevDocs AI was built to solve this exact problem by providing an intelligent, conversational interface to any technical document set.

## ✨ Features

- **Instant & Accurate Answers:** Ask complex questions in natural language and get precise answers grounded in the source documentation.
- **RAG Pipeline from Scratch:** Implements a Retrieval-Augmented Generation pipeline from its foundational components to ensure factual accuracy and prevent model hallucination.
- **Custom Semantic Search:** Utilizes a custom-built vector search engine to understand the *intent* behind a query, not just keywords.
- **Interactive Interface:** A simple and clean UI built with Streamlit for easy interaction.

## 🛠️ Tech Stack & Core Libraries

- **Core Logic:** Python, NumPy
- **Embeddings & LLM:** Hugging Face (Sentence-Transformers, Transformers)
- **Frontend:** Streamlit

## 🧠 Core Architecture & Implementation

This project was built from foundational components to demonstrate a deep, first-principles understanding of RAG systems.

- **Custom Vector Search:** Instead of relying on a pre-built library like FAISS or Pinecone, the retrieval mechanism was implemented **from scratch**. The system uses a Hugging Face model to generate embeddings, which are stored in a simple in-memory list. The core search logic is a custom Python function that calculates the **cosine similarity** between the query and document embeddings using **NumPy**.

- **Manual Orchestration:** The entire RAG pipeline—`retrieve -> generate`—is orchestrated with a custom Python script, managing the flow of data between the vector store, the prompt template, and the final call to the Hugging Face LLM.

## 📊 Evaluation

The model's performance was evaluated on a test set of technical questions not seen during development.

- **Metric:** ROUGE-L (measures the overlap between the generated answer and a reference).
- **Average Score:** **~0.10**

This score indicates a strong ability to retrieve relevant context and generate factually grounded, concise answers.

## 🚀 How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/AnasSayed27/AI-ML-Portfolio.git
    ```
2.  **Navigate to the Project Folder:**
    ```bash
    cd AI-ML-Portfolio/DevDocs-AI-RAG-Chatbot
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit App:**
    ```bash
    streamlit run app.py
    ```
