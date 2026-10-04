from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os
import shutil


from pdf_manager import extract_text_from_pdf, create_chuncks
from rag import RAGSystem
from ai import(
    answer_question,
    generate_summary,
    generate_quiz,
    generate_flashcards
)    

app = FastAPI(
    title="OpenStudy AI",
    description="Open-source AI powered study assistant",
    version="1.0.0"
)

"""
for the Cross-Origin Resource Sharing.
this is the code below

"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
this is for the directories
"""

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

"""
For the RAG system, we create an instance of the RAGSystem class.

"""
rag = RAGSystem()


"""
for the models, we define a QuestionRequest model that represents the request body for the /ask endpoint. It contains a question field of type str.

"""
class QuestionRequest(BaseModel):
    question:str

"""
for the home route, we define a GET endpoint at the root URL ("/") that returns a simple message indicating that the OpenStudy AI API is running.

"""
@app.get("/")
def home():
    return{
        "message": "OpenStudy AI API is running......."
    }

