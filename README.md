# Text Image to PDF Translator

The "Text Image to PDF Translator" is a Python script designed to convert images containing text into translated PDF files. It utilizes image processing, text translation, and PDF generation libraries to achieve this task.

## Features

- Converts images containing text to PDF files with translated text.
- Supports translation to multiple languages using the Google Translate API.
- Flexible and customizable translation options.
- Easy-to-use command-line interface.
- Cross-platform compatibility.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/text-image-to-pdf-translator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd text-image-to-pdf-translator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure that the `qpdf.sh` script has execute permissions:

    ```bash
    chmod +x qpdf.sh
    ```

## Usage

To use the program, follow these steps:

:

    ```bash
    python im_t_pdf_tr.py
    ```
## Dependencies

- Python 3.x
- requests
- reportlab
- googletrans
- arabic_reshaper
- bidi
- qpdf (for certain structural fixes in PDFs)


## Installation

1. Clone or download the repository.
2. Install the required Python packages by running:
pip install -r requirements.txt

markdown
Copy code
3. Obtain API keys for OCR.Space and Google Translate.
4. Place the QPDF tool in your system's path or provide the correct path in the script.

## Usage

1. Place the PNG images containing the text in the specified directory (`pngs` by default).
2. Run the script `im_t_pdf_tr.py`.
3. The script will extract text from each image, translate it to the specified language, and save the translated PDFs in the output directory (`translated_pdfs` by default).

## Configuration

- You can specify the target language for translation by changing the `target_language` variable in the script.
- Replace the placeholder `'YOUR_API_KEY'` with your actual API key for OCR.Space.
