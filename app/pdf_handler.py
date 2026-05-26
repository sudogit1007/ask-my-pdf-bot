import fitz
def read_pdf(pdf_file):
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")

    text_chunks = []

    for page_number in range(len(document)):
        page = document[page_number]
        content = page.get_text()

        if content.strip():
            text_chunks.append(
                {
                    "text": content,
                    "page": page_number + 1
                }
            )

    return text_chunks