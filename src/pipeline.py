

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
