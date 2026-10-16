from pathlib import Path

from docx import Document
from pypdf import PdfReader


SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}


def extract_pdf_text(uploaded_file) -> str:
    """Extract text from an uploaded PDF file."""
    reader = PdfReader(uploaded_file)

    pages = [
        page.extract_text() or ""
        for page in reader.pages
    ]

    return "\n".join(pages).strip()


def extract_docx_text(uploaded_file) -> str:
    """Extract text from an uploaded Microsoft Word document."""
    document = Document(uploaded_file)

    paragraphs = [
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n".join(paragraphs).strip()


def extract_txt_text(uploaded_file) -> str:
    """Extract text from an uploaded plain-text file."""
    content = uploaded_file.read()

    if isinstance(content, bytes):
        content = content.decode("utf-8", errors="replace")

    return content.strip()


def extract_text_from_file(uploaded_file) -> str:
    """Choose the correct text extractor based on the file extension."""
    extension = Path(uploaded_file.name).suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            "Unsupported file type. Please upload a PDF, DOCX, or TXT file."
        )

    uploaded_file.seek(0)

    if extension == ".pdf":
        return extract_pdf_text(uploaded_file)

    if extension == ".docx":
        return extract_docx_text(uploaded_file)

    return extract_txt_text(uploaded_file)