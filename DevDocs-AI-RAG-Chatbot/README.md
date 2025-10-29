# DevDocs AI: An Intelligent Q&A Bot for Technical Documentation

## 🎯 The Problem

Developers spend a significant amount of time manually searching through dense and complex technical documentation. This is a major bottleneck that breaks concentration and slows down the development process. DevDocs AI was built to solve this exact problem by providing an intelligent, conversational interface to any technical document set.

## ✨ Features

- **Instant & Accurate Answers:** Ask complex questions in natural language and get precise answers grounded in the source documentation.
- **RAG Pipeline:** Utilizes a robust Retrieval-Augmented Generation pipeline to ensure factual accuracy and prevent model hallucination.
- **Semantic Search:** Understands the *intent* behind a query, not just keywords, to find the most relevant information.
- **Interactive Interface:** A simple and clean UI built with Streamlit for easy interaction.

## 🛠️ Tech Stack

- **Core Pipeline:** Python, LangChain
- **Embeddings & LLM:** Hugging Face Transformers
- **Vector Store:** FAISS for high-speed similarity search
- **Frontend:** Streamlit

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/AnasSayed27/AI-ML-Portfolio.git
   cd AI-ML-Portfolio/DevDocs-AI-RAG-Chatbot
