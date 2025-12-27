

import pandas as pd
import os

def extract_medicine_data():
    """
    Extracts medicine/drug data from local CSV.
    """
    csv_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "sample_clinicaltrials.csv"
    )
)

    if not os.path.exists(csv_path):
        print(f"❌ CSV file not found: {csv_path}")
        return pd.DataFrame()

    df = pd.read_csv(csv_path)

    # Rename key columns to standard names
    df = df.rename(columns={
        "id": "medicine_id",
        "name": "name",
        "price": "price",
        "Is_disconti": "is_discontinued",
        "manufactu": "manufacturer",
        "type": "type",
        "pack_size": "pack_size",
        "short_com": "short_com_1",
        "short_com_1": "short_com_2",
        "salt_comp": "salt_composition",
        "medicine_": "medicine_name",
        "side_effec": "side_effects",
        "drug_interactions": "drug_interactions"
    })

    # Ensure all expected columns exist
    expected_cols = ["medicine_id","name","price","is_discontinued","manufacturer",
                     "type","pack_size","short_com_1","short_com_2","salt_composition",
                     "medicine_name","side_effects","drug_interactions"]
    for col in expected_cols:
        if col not in df.columns:
            df[col] = pd.NA

    return df[expected_cols]
