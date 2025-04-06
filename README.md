# 🧠 OCR Text Extractor

An AI-powered Python tool that extracts structured data (text, tables, and key-value pairs) from **PDFs or images**, detects the **language**, and exports it as:
- 📄 JSON
- 📊 Excel
- 🧾 PDF Report

> Built with ❤️ by [Maryem Hadj Wannes](https://github.com/MaryemHadjWannes)

---

## 🚀 Features

✅ Extract text from images or PDFs  
✅ Preprocess images for better OCR accuracy  
✅ Detect document language (multi-lingual support)  
✅ Extract key-value pairs (like name, email, date, etc.)  
✅ Detect and export tables (invoices, records, etc.)  
✅ Export results as JSON, Excel, or PDF reports  
✅ Clean and modular code structure (easy to extend)

---

## 📦 Tech Stack

- `Python`
- `OpenCV`
- `pytesseract`
- `pdf2image`
- `langdetect`
- `pandas`
- `reportlab`

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/MaryemHadjWannes/ocr-text-extractor.git
cd ocr-text-extractor
```

Make sure you have Tesseract OCR installed on your system.


# Create a virtual environment (optional)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


## 🧪 Usage
```bash
# Format: python main.py <file_path> <output_name>

python3 main.py "samples/image1.png" image1
```

This will generate:

- `output/image1.json`

- `output/image1.xlsx`

- `output/image1_report.pdf`


## 📂 Project Structure
```bash
ocr_text_extractor/
├── main.py
├── ocr/
│   ├── text_extraction.py
│   ├── preprocessing.py
│   ├── structure_detection.py
│   └── language_detection.py
├── exporters/
│   ├── json_exporter.py
│   ├── excel_exporter.py
│   └── report_generator.py
├── samples/
└── output/
```
  

