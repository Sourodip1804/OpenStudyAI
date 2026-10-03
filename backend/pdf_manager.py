# this is the library for pdf management
import fitz

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)

    # let pages be a list 
    pages =[]
