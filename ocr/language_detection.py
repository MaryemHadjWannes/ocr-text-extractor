# ocr/language_detection.py

from langdetect import detect, DetectorFactory

# Fix randomness in results
DetectorFactory.seed = 0

class LanguageDetector:
    def __init__(self):
        pass

    def detect_language(self, text: str) -> str:
        try:
            language = detect(text)
            return language
        except Exception:
            return "unknown"
