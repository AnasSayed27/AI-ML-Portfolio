# RAG Ethics Q&A Chatbot (Generative AI Prototype)

My first hands-on GenAI project: A Retrieval-Augmented Generation (RAG) system for answering AI ethics queries. Built using Hugging Face Transformers, Sentence Transformers for embeddings, and GPT-2 for grounded text generation. Inspired by Coursera's "Generative AI with LLMs" (audited/completed).

## Why RAG?
- Retrieves relevant facts from a custom ethics dataset to reduce LLM hallucinations.
- End-to-end pipeline: Embed → Retrieve (cosine similarity) → Generate.

## Key Features & Results
- Dataset: 20+ AI ethics facts (e.g., bias, privacy).
- Metrics: Avg ROUGE-L score: 0.52 on 10 test queries (e.g., "What is AI bias?" → Accurate, context-based answer).
- Tools: Python, NumPy, Transformers (no heavy training—runs in Colab).

| Query Example | Retrieved Context | Generated Answer | ROUGE Score |
|---------------|-------------------|------------------|-------------|
| What causes AI bias? | "AI bias occurs when models learn unfair patterns..." | "AI bias stems from skewed training data leading to unfair outputs." | ~0.10 |

## Setup & Run
1. Clone: `git clone https://github.com/Sober-Human/AI-ML-Portfolio`
2. Open `RAG_Ethics_Chatbot.ipynb` in Colab/Jupyter.
3. Install: `!pip install transformers sentence-transformers datasets rouge-score`
4. Run cells—query the bot!

<image-card alt="Demo" src="demo.gif" ></image-card>  <!-- Add your GIF here -->

## Learnings
- Applied prompt engineering for context grounding.
- Next: Scale with FAISS for larger DBs; fine-tune LLM.

Questions? [LinkedIn](www.linkedin.com/in/soberhuman).
