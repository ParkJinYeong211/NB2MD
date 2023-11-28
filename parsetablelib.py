import pandas as pd

def assign_header(df):
    df = pd.DataFrame(df)
    df.columns=df.iloc[0]
    return df[1:]

def setIO():
    return _set_read_path(), _set_write_path()

def _set_read_path():
    return input("Ensure file is in current directory: ")

def _set_write_path():
    return input("Specify filename to write to: ")

def check_if_list(x):
    if isinstance(x, list):
        return x
    else:
        return [x, ]