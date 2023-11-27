from docx import Document
import parsetablelib as ptl
import pandas as pd

class DTParser:

    def __init__(self) -> None:
        self._read_path = input("Ensure file is in current directory: ")
        self._tables = Document(self._read_path).tables
        self._write_path = input("Specify filename to write to: ")
        self.convert_to_DF()
        

    def convert_to_DF(self):
        output = []
        for table in self._tables:
            df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
            for i, row in enumerate(table.rows):
                for j, cell in enumerate(row.cells):
                    if cell.text:
                        df[i][j] = cell.text
            output.append(pd.DataFrame(df))
        self._tables = output


    def gen_output(self):
        for t, table in enumerate(self._tables):
                with open(self._write_path, 'a',encoding="utf-8") as f:
                    f.write(f"\n\n# Table {t}\n")
                    for row in table.to_markdown():
                        f.write(row)