# exporters/excel_exporter.py

import pandas as pd
from typing import List

class ExcelExporter:
    def __init__(self):
        pass

    def save_table_to_excel(self, table: List[List[str]], output_path: str) -> None:
        if not table:
            print("No table data to export.")
            return

        df = pd.DataFrame(table[1:], columns=table[0])
        df.to_excel(output_path, index=False)
