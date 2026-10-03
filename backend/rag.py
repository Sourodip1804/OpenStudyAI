# this is a Retrieval-Augmented Generation(RAG) 

import faiss
# this is for the library for quickly finding the most similar vectors in a large collection, and it fits right into the chunking project you've been working on.

import numpy as np
from sentence_transformers import SentenceTransformer

class RAGSystem:
    def __init__(self):
        print("Loading embedding model ....")
        self.embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )