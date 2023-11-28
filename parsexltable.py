import pandas as pd
import parsetablelib as ptl
import writer

class XTParser:

    def __init__(self) -> None:
        self._read_path, self._write_path = ptl.setIO()
        self._tables = (pd.read_excel(self._read_path))
        self._tables = ptl.check_if_list(self._tables)
        self._writer = writer.Writer(self._write_path)

    def gen_output(self):
        self._writer.write(self._tables)