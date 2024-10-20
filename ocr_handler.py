import os
import re
import pdfplumber
import requests
from pdf2image import convert_from_path

from config import GEMINI_API_ENDPOINT, GEMINI_API_KEY

def gemini_ocr(image_path):
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        headers = {'Authorization': f'Bearer {GEMINI_API_KEY}'}
        response = requests.post(GEMINI_API_ENDPOINT, headers=headers, files=files)
        
        if response.status_code == 200:
            return response.json().get("text", "")
        else:
            print(f"Error with Gemini API: {response.status_code}, {response.text}")
            return ""

def extract_text_from_pdf(file_path):
    text_content = ""
    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
        
        if not text.strip():
            images = convert_from_path(file_path, first_page=page_num + 1, last_page=page_num + 1)
            temp_image_path = f"temp_page_{page_num}.png"
            images[0].save(temp_image_path, "PNG")
            text += gemini_ocr(temp_image_path)
            os.remove(temp_image_path)

        text_content += text
    return text_content
