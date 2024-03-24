import os
import requests
from reportlab.lib import colors
import uuid  # Import UUID module to generate unique filenames
from googletrans import Translator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display
from fpdf import FPDF

import os
import subprocess
def modify_pdf_files(directory):
    # Get a list of PDF files in the directory
    pdf_files = [file for file in os.listdir(directory) if file.endswith(".pdf")]

    # Iterate over each PDF file
    for pdf_file in pdf_files:
        # Construct the path to the PDF file
        pdf_path = os.path.join(directory, pdf_file)

        # Execute the bash script on the PDF file
        bash_command = ["qpdf", "--replace-input", pdf_path]
        subprocess.run(bash_command, check=True)

def extract_text_from_image(image_path, api_key):
    payload = {'apikey': api_key}
    with open(image_path, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image', files={image_path: f}, data=payload)
    if r.status_code == 200:
        result = r.json()
        if result['IsErroredOnProcessing']:
            print("Error processing image:", result['ErrorMessage'])
            return ""
        else:
            return result['ParsedResults'][0]['ParsedText']
    else:
        print("HTTP Error:", r.status_code)
        return ""

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


def remove_special_characters(text):
    return text.replace("■", "").strip()

def is_headline(line, next_line):
    # Check if the line starts with a capital letter and has two or three words
    if line :
        words = line.split()
        if 2 <= len(words) <= 3:
            return True
    return False


def save_to_pdf(text, output_pdf):
    pdf = FPDF()
    pdf.add_page()
    
    # Add a font that supports Arabic text
    pdf.add_font('Arial', '', 'arial.ttf', uni=True)
    font_family = "Arial"  # Example font family
    font_style = ""  # Example font style (empty for regular)
    font_size = 12  # Example font size
    pdf.set_font(font_family, font_style, font_size)
    # Split text into paragraphs
  
    paragraphs = text.split("\n\n")
    y = 750  # Initial y-coordinate
    first_headline = True  # Flag to track the first headline
    for paragraph in paragraphs:
        lines = paragraph.split("\n")
        if all(line.strip() == "" for line in lines):
            continue  # Skip drawing if all lines are empty
        for line_index, line in enumerate(lines):
            # Remove special characters from the end of the line
            red = 0
            green = 0
            blue = 0
            line = remove_special_characters(line)
            x = 185
            # Get the next line if available
            next_line = lines[line_index + 1] if line_index + 1 < len(lines) else ""
            # Check if the line is a headline
            font_size = 10  # Bigger font size for headlines
            if is_headline(line, next_line):
                red = 255
                green = 0
                blue = 0 # Color for headlines
                if first_headline:
                    x = 90
                    pdf.set_font("Arial","", 16)
                    first_headline = False
                else:
                    pdf.set_font("Arial","",font_size)
                if not first_headline:
                    y = 15
            else:
                pdf.set_font("Arial","",font_size)
            # Set color for headline
            pdf.set_text_color(red, green, blue)
            # Draw the line on the canvas
            reshaped_text = arabic_reshaper.reshape(line)    # correct its shape
            bidi_text = get_display(reshaped_text)
            pdf.cell(x, y, txt=bidi_text, ln=True, align='R')
            # Adjust y-coordinate for the next line
            y = 6  # Adjust line spacing as needed

    pdf.output(output_pdf)
    # Save the PDF to file
def main():
    # Directory containing PNG images
    png_dir = "./pngs"
    # API key for OCR.Space (Replace 'YOUR_API_KEY' with your actual API key)
    api_key = "K86200021888957"
    # Target language for translation
    target_language = "ar"  # Change this to your desired language code
    # Directory to save the translated PDFs
    output_dir = "./translated_pdfs"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for png_file in os.listdir(png_dir):
        if png_file.endswith(".png"):
            png_path = os.path.join(png_dir, png_file)
            text = extract_text_from_image(png_path, api_key)
            translated_text = translate_text(text, target_language)

            # Generate a unique filename for the translated PDF
            pdf_filename = str(uuid.uuid4()) + ".pdf"
            pdf_path = os.path.join(output_dir, pdf_filename)

            # Save the translated text to PDF
            save_to_pdf(translated_text, pdf_path)

            print("Translated text saved to", pdf_path)
    modify_pdf_files("./translated_pdfs")

if __name__ == "__main__":
    main()
