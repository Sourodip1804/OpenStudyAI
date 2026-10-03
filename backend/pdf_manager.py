# this is the library for pdf management
import fitz

# defining the function to extract text from pdf file

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)

    # let pages be a list 
    pages =[]

    # here enumerate gives the number of pages and the page object
    for page_number, page in enumerate(document):
        text=page.get_text("text")
        if text.strip():
            pages.append({
                "page": page_number + 1,
                "text": text.strip()
            })
    document.close()
    return pages

