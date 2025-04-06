# exporters/report_generator.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from typing import Dict, List

class ReportGenerator:
    def __init__(self):
        pass

    def generate_pdf_report(self, output_path: str, title: str, data: Dict[str, str], table: List[List[str]], language: str = "unknown"):
        c = canvas.Canvas(output_path, pagesize=A4)
        width, height = A4
        y = height - 50

        # Title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, f"📄 Report: {title}")
        y -= 30

        # Language
        c.setFont("Helvetica", 10)
        c.drawString(50, y, f"Detected Language: {language}")
        y -= 20

        # Key-Value Data
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "Extracted Information:")
        y -= 20
        c.setFont("Helvetica", 10)
        for key, value in data.items():
            c.drawString(60, y, f"{key}: {value}")
            y -= 15
            if y < 100:
                c.showPage()
                y = height - 50

        # Table
        if table:
            y -= 20
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y, "Detected Table:")
            y -= 20
            c.setFont("Helvetica", 10)
            for row in table:
                c.drawString(60, y, " | ".join(row))
                y -= 15
                if y < 100:
                    c.showPage()
                    y = height - 50

        c.save()
