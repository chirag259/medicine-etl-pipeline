"""
import pandas as pd

def clean_studies(df):
    # Basic cleaning: remove empty ids, dedupe, parse dates
    df = df.dropna(subset=["study_id"])
    df = df.drop_duplicates(subset=["study_id"])
    df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce").dt.date
    df["title"] = df["title"].fillna("").str.strip()
    df["status"] = df["status"].apply(lambda s: s[0] if isinstance(s, list) else s)
    df["phase"] = df["phase"].apply(lambda p: p[0] if isinstance(p, list) else p)
    df["sponsor"] = df["sponsor"].apply(lambda s: s[0] if isinstance(s, list) else s)
    return df

"""
import pandas as pd

def clean_medicine_data(df):
    """
    Cleans medicine/drug DataFrame.
    - Removes rows without medicine_id or name
    - Fills missing values where necessary
    """
    df = df.dropna(subset=["medicine_id", "name"])

    # Optional: fill missing numeric values
    df["price"] = df["price"].fillna(0)

    # Optional: standardize boolean column
    #df["is_discontinued"] = df["is_discontinued"].fillna(False)

    df["is_discontinued"] = (
    df["is_discontinued"]
    .astype("boolean")
    .fillna(False)
)


    df = df.where(pd.notna(df), None)

    return df
