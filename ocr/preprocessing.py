# ocr/preprocessing.py

import cv2
import numpy as np

class ImagePreprocessor:
    def __init__(self):
        pass

    def preprocess(self, image_path: str) -> any:
        img = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply thresholding (binarization)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        return thresh
