import pandas as pd

def assign_header(df):
    df = pd.DataFrame(df)
    df.columns=df.iloc[0]
    return df[1:]