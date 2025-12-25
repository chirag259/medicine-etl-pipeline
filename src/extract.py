"""
import requests
import pandas as pd

def download_clinicaltrials_sample():
    # Example: use ClinicalTrials.gov API (simple sample)
    url = "https://clinicaltrials.gov/api/query/study_fields?expr=cancer&fields=NCTId,BriefTitle,Condition,StartDate,OverallStatus,Phase,SponsorName&min_rnk=1&max_rnk=100&fmt=json"
    r = requests.get(url, timeout=30)
    data = r.json()
    studies = data["StudyFieldsResponse"]["StudyFields"]
    df = pd.json_normalize(studies)
    # rename and clean columns
    df = df.rename(columns={
        "NCTId": "study_id",
        "BriefTitle": "title",
        "StartDate": "start_date",
        "OverallStatus": "status",
        "Phase": "phase",
        "SponsorName": "sponsor"
    })
    return df[["study_id","title","status","phase","start_date","sponsor"]]
"""  
"""
import requests
import pandas as pd
import os

def download_clinicaltrials_sample():

    Downloads clinical trials data from ClinicalTrials.gov.
    Falls back to a local CSV if API fails or returns no data.
    
    url = "https://clinicaltrials.gov/api/query/study_fields?expr=cancer&fields=NCTId,BriefTitle,Condition,StartDate,OverallStatus,Phase,SponsorName&min_rnk=1&max_rnk=100&fmt=json"
    
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # Raise error if status code != 200
        data = r.json()
        studies = data.get("StudyFieldsResponse", {}).get("StudyFields", [])
        if studies:
            df = pd.json_normalize(studies)
            df = df.rename(columns={
                "NCTId": "study_id",
                "BriefTitle": "title",
                "StartDate": "start_date",
                "OverallStatus": "status",
                "Phase": "phase",
                "SponsorName": "sponsor"
            })
            return df[["study_id","title","status","phase","start_date","sponsor"]]
        else:
            print("⚠️ API returned no studies, falling back to CSV.")
    except Exception as e:
        print(f"❌ API request failed: {e}")
    
    # Fallback to local CSV
    csv_path = os.path.join(os.path.dirname(__file__), "sample_clinicaltrials.csv")
    if os.path.exists(csv_path):
        print(f"📄 Loading data from local CSV: {csv_path}")
        df = pd.read_csv(csv_path)
        return df
    else:
        print("❌ No local CSV found. Returning empty DataFrame.")
        return pd.DataFrame()


"""

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
