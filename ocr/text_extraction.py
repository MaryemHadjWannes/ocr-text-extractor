# ocr/text_extraction.py

import pytesseract
import cv2
from pdf2image import convert_from_path
import os
from typing import List
from .preprocessing import ImagePreprocessor

class TextExtractor:
    def __init__(self):
        self.preprocessor = ImagePreprocessor()

    def extract_text_from_image(self, image_path: str) -> str:
        processed_img = self.preprocessor.preprocess(image_path)
        text = pytesseract.image_to_string(processed_img)
        return text

    def extract_text_from_pdf(self, pdf_path: str) -> List[str]:
        images = convert_from_path(pdf_path)
        text_list = []

        for i, img in enumerate(images):
            img_path = f"temp_page_{i}.png"
            img.save(img_path, "PNG")
            text = self.extract_text_from_image(img_path)
            text_list.append(text)
            os.remove(img_path)

        return text_list
