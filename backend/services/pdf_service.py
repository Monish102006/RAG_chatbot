import pymupdf
# fitz is deprecated, so using pymupdf

def extract_text_from_pdf(pdf_path):
    document = pymupdf.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text
    
def extract_pages_from_pdf(pdf_path):
    document = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        page_text = page.get_text()

        pages.append({
            "page_number": page_number,
            "text": page_text
        })

    document.close()

    return pages