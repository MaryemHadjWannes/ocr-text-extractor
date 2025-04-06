# exporters/json_exporter.py

import json

class JSONExporter:
    def __init__(self):
        pass

    def save_to_json(self, data: dict, output_path: str) -> None:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
