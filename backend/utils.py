from io import BytesIO

import PyPDF2


def extract_text_from_pdf(pdf_bytes: BytesIO) -> str:
    """
    Extract text from a PDF file.

    Parameters
    ----------
    pdf_bytes : BytesIO
        The PDF file as a BytesIO object.

    Returns
    -------
    pdf_text : str
        The extracted text from the PDF file.

    Raises
    ------
    ValueError
        If the provided PDF file is empty or invalid.

    Notes
    -----
    This function uses the PyPDF2 library to extract text from a PDF file.
    It assumes that the PDF file is in a valid format and can be read.

    Examples
    --------
    >>> from io import BytesIO
    >>> pdf_bytes = BytesIO(b'%PDF-1.7\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 27 >>\nstream\nBT\n/F1 12 Tf\n100 100 Td\n(Hello, World!) Tj\nET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f\n0000000010 00000 n\n0000000053 00000 n\n0000000103 00000 n\n0000000174 00000 n\ntrailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n227\n%%EOF\n')
    >>> extract_text_from_pdf(pdf_bytes)
    'Hello, World!'
    """

    try:
        reader = PyPDF2.PdfReader(pdf_bytes, )
        if len(reader.pages) == 0:
            raise ValueError("PDF is empty")

        pdf_text = ""
        for i in range(len(reader.pages)):
            pdf_text += reader.pages[i].extract_text()
            print(pdf_text)
        return pdf_text

    except PyPDF2.PdfError as e:
        raise ValueError(f"Invalid file: {e}")

    # TODO: Use PyPDF2.PdfReader to open the input `pdf_bytes` and extract the text from each page appended to `pdf_text`.
    # Hint: Use the `extract_text()` method of the `PyPDF2.PdfReader` object.


with open('backend\\Federico_FERREYRA_CV_EN.pdf', 'rb') as pdf:
    extract_text_from_pdf(pdf)
