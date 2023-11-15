from docx import Document
import parsetablelib as ptl

class DTParser:

    def __init__(self) -> None:
        self._read_path = input("Ensure file is in current directory: ")
        self._tables = Document(self._read_path).tables

        self._write_path = input("Specify filename to write to: ")



    def gen_output(self):
        for t, table in enumerate(self._tables[:20]):
            converted_table = ptl.xtable(table)
            with open(self._write_path, 'a',encoding="utf-8") as f:
                f.write(f"\n\n# Table {t}\n")
                for row in converted_table:
                    f.write(row)