from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from httpcore import request
from pydantic import BaseModel

import os
import shutil


from pdf_manager import extract_text_from_pdf, create_chunks
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

"""
Upload PDF Endpoint: This endpoint allows users to upload a PDF file. The uploaded file is saved to the UPLOAD_DIR, and the text is extracted from the PDF. The extracted text is then chunked into smaller pieces, and the RAG system creates an index of these chunks for retrieval.

"""
@app.post("/upload")

async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    try:

        pages = extract_text_from_pdf(file_path)

        if not pages:

            raise HTTPException(
                status_code=400,
                detail="Could not extract text from PDF"
            )

        chunks = create_chunks(pages)

        rag.create_index(chunks)

        return {
            "message": "PDF uploaded successfully",
            "filename": file.filename,
            "pages": len(pages),
            "chunks": len(chunks)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


"""
for asking the question

"""

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be Empty...."
        )
    relevant_chunks = rag_search(
      request.question,
      top_k=5
  )  
    if not relevant_chunks:

        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF first"
        )

    context = "\n\n".join(
        [
            f"[Page {chunk['page']}]\n{chunk['text']}"
            for chunk in relevant_chunks
        ]
    )

    answer = answer_question(
        request.question,
        context
    )

    sources = [
        {
            "page": chunk["page"]
        }
        for chunk in relevant_chunks
    ]

    return {
        "answer": answer,
        "sources": sources
    }