from docx import Document
import parsetablelib as ptl
import writer
import pandas as pd

class DTParser:

    def __init__(self) -> None:
        self._read_path, self._write_path = ptl.setIO()
        self._tables = Document(self._read_path).tables
        self.convert_to_DF()
        self._writer = writer.Writer(self._write_path)
        

    def convert_to_DF(self):
        output = []
        for table in self._tables:
            df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
            for i, row in enumerate(table.rows):
                for j, cell in enumerate(row.cells):
                    if cell.text:
                        df[i][j] = cell.text
            df = ptl.assign_header(df)
            output.append(df)
        self._tables = output


    def gen_output(self):
        self._writer.write(self._tables)