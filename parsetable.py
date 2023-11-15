from docx import Document
import parsetablelib as ptl
read_path = input("Ensure file is in current directory (or specify relative or absolute path): ")
tables = Document(read_path).tables

write_path = input("Specify location to write to: ")



def gen_output(tables):
    for t, table in enumerate(tables[:20]):
        converted_table = ptl.xtable(table)
        with open(write_path, 'a',encoding="utf-8") as f:
            f.write(f"\n\n# Table {t}\n")
            for row in converted_table:
                f.write(row)


gen_output(tables)

