# main.py

import sys
from ocr.text_extraction import TextExtractor
from ocr.language_detection import LanguageDetector
from ocr.structure_detection import StructureDetector
from exporters.json_exporter import JSONExporter
from exporters.excel_exporter import ExcelExporter
from exporters.report_generator import ReportGenerator

def main(file_path: str, output_name: str):
    print("🚀 Starting OCR Text Extractor...")

    extractor = TextExtractor()
    detector = LanguageDetector()
    structure = StructureDetector()
    json_exporter = JSONExporter()
    excel_exporter = ExcelExporter()
    report_generator = ReportGenerator()

    # Extract text
    if file_path.lower().endswith(".pdf"):
        text_pages = extractor.extract_text_from_pdf(file_path)
        full_text = "\n".join(text_pages)
    else:
        full_text = extractor.extract_text_from_image(file_path)

    # Detect language
    language = detector.detect_language(full_text)
    print(f"🌍 Detected Language: {language}")

    # Extract structured data
    headings = structure.extract_headings(full_text)
    key_values = structure.extract_key_value_pairs(full_text)
    table = structure.extract_table(full_text)

    # Export everything
    json_exporter.save_to_json(key_values, f"output/{output_name}.json")
    excel_exporter.save_table_to_excel(table, f"output/{output_name}.xlsx")
    report_generator.generate_pdf_report(
        output_path=f"output/{output_name}_report.pdf",
        title=output_name,
        data=key_values,
        table=table,
        language=language
    )

    print("✅ Done! Files saved to output folder.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_file_path> <output_name>")
    else:
        main(sys.argv[1], sys.argv[2])
