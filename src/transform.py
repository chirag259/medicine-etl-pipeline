
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
    

    df["is_discontinued"] = (
    df["is_discontinued"]
    .astype("boolean")
    .fillna(False)
)


    df = df.where(pd.notna(df), None)

    return df
