from docx import Document

def get_colmax(t):
    colmax = []

    for col in t.columns:
        max = 0
        for c in col.cells:
            cellwid = len(c.text)
            #print(f"|{c.text}|")
            max = cellwid if cellwid > max else max
            #print(f"cellwid = {cellwid}; max = {max}")
        colmax.append(max)
    #print(colmax)
    
    return colmax

def get_parsed_row(row, colmax):
    return "| "+"| ".join(c.text.ljust(colmax[i]+1) for i, c in enumerate(row.cells))+"|\n"

def header_spacer_row(colmax):
    return "|-"+"|-".join("-"*(c+1) for c in colmax)+"|\n"

def xtable(t):

    output_table = []
    colmax = get_colmax(t)

    for r, row in enumerate(t.rows):
        if r == 1:
            output_table.append(header_spacer_row(colmax))
        parsed_row = get_parsed_row(row, colmax)
        output_table.append(parsed_row)

    return output_table