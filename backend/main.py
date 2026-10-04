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
