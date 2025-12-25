"""
from extract import download_clinicaltrials_sample
from transform import clean_studies
from load import upsert_sponsors, upsert_studies

def run_pipeline():
    print("🚀 Starting ETL pipeline")

    # 1️⃣ Extract
    df_raw = download_clinicaltrials_sample()
    print(f"✅ Extracted {len(df_raw)} rows")

    # 2️⃣ Transform
    df_clean = clean_studies(df_raw)
    print(f"✅ Cleaned to {len(df_clean)} rows")

    # 3️⃣ Load - Sponsors
    upsert_sponsors(df_clean)
    print("✅ Sponsors loaded")

    # 4️⃣ Load - Studies
    upsert_studies(df_clean)
    print("🎉 Studies loaded")

if __name__ == "__main__":
    run_pipeline()
"""
"""
from extract import download_clinicaltrials_sample
from transform import clean_studies
from load import upsert_sponsors, upsert_studies

def run_pipeline():
    print("🚀 Starting ETL pipeline")

    # 1️⃣ Extract
    df_raw = download_clinicaltrials_sample()
    print(f"✅ Extracted {len(df_raw)} rows")

    if df_raw.empty:
        print("⚠️ No data to process. Exiting pipeline.")
        return

    # 2️⃣ Transform
    df_clean = clean_studies(df_raw)
    print(f"✅ Cleaned to {len(df_clean)} rows")

    # 3️⃣ Load - Sponsors
    upsert_sponsors(df_clean)
    print("✅ Sponsors loaded")

    # 4️⃣ Load - Studies
    upsert_studies(df_clean)
    print("🎉 Studies loaded")

if __name__ == "__main__":
    run_pipeline()
"""

from extract import extract_medicine_data
from transform import clean_medicine_data
from load import upsert_medicine

def run_pipeline():
    print("🚀 Starting Medicine ETL pipeline")

    df_raw = extract_medicine_data()
    print(f"✅ Extracted {len(df_raw)} rows")

    if df_raw.empty:
        print("⚠️ No data to process")
        return

    df_clean = clean_medicine_data(df_raw)
    print(f"✅ Cleaned to {len(df_clean)} rows")

    upsert_medicine(df_clean)
    print("🎉 Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
