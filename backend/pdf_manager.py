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

def create_chunks(pages, chunk_size=500, overlap=100):
    # this is for the separating the word of the pdf into chunks of 500 words with an overlap of 100 words
    chunks=[] #taking this as list to store the chunks
    for page in pages:
        words = page["text"].split()
        start=0

        while start < len(words):
            end=start + chunk_size
            chunk_words=words[start:end]
            if chunk_words:
                chunks.append({
                    "text": " ".join(chunk_words),
                    "page": page["page"]
                })
            start += chunk_size - overlap
    return chunks

