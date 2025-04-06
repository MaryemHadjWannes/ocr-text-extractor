import re
from typing import Dict, List

class StructureDetector:
    def __init__(self):
        pass

    def extract_key_value_pairs(self, text: str) -> Dict[str, str]:
        result = {}
        lines = text.splitlines()
        buffer_key = None

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Case: key: value in one line
            if ":" in line:
                key, value = line.split(":", 1)
                result[key.strip()] = value.strip()
                buffer_key = None
            elif buffer_key:
                # Safely append continuation to last key
                if buffer_key in result:
                    result[buffer_key] += " " + line
                else:
                    # fallback: store line as value
                    result[buffer_key] = line
                buffer_key = None
            else:
                # Check for potential header-style line (e.g., "NAME")
                if re.match(r"^[A-Z][A-Za-z\s]+$", line):
                    buffer_key = line
                else:
                    buffer_key = None  # ignore non-matching lines

        return result

    def extract_table(self, text: str) -> List[List[str]]:
        rows = []
        lines = text.splitlines()

        # Attempt to find start of table (contains "Description" and "Amount")
        table_started = False
        for line in lines:
            if not table_started and ("Description" in line and "Amount" in line):
                headers = re.split(r"\s{2,}", line.strip())
                rows.append(headers)
                table_started = True
                continue

            if table_started:
                if line.strip() == "" or len(line.strip()) < 4:
                    continue
                row = re.split(r"\s{2,}", line.strip())
                if len(row) >= 2:
                    rows.append(row)

        return rows

    def extract_headings(self, text: str) -> List[str]:
        lines = text.splitlines()
        headings = [line.strip() for line in lines if line.isupper() and len(line.strip()) > 3]
        return headings

    def extract_to_section(self, text: str) -> str:
        """
        Detect 'To' section in invoice
        """
        lines = text.splitlines()
        start = False
        to_block = []

        for line in lines:
            if "To" in line.strip():
                start = True
                continue
            if start:
                if line.strip() == "":
                    break
                to_block.append(line.strip())

        return "\n".join(to_block)
