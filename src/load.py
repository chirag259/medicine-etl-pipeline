

from db import get_engine
from sqlalchemy import text

engine = get_engine()

def upsert_medicine(df):
    """
    Bulk UPSERT medicine data into MySQL using existing engine.
    """
    if df.empty:
        print("⚠️ No medicine data to load")
        return

    table_name = "medicines"

    with engine.begin() as conn:
        # Create table if not exists
        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                medicine_id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255),
                price FLOAT,
                is_discontinued BOOLEAN,
                manufacturer VARCHAR(255),
                type VARCHAR(100),
                pack_size VARCHAR(100),
                short_com_1 VARCHAR(255),
                short_com_2 VARCHAR(255),
                salt_composition VARCHAR(255),
                medicine_name VARCHAR(255),
                side_effects TEXT,
                drug_interactions TEXT
            )
        """))

        # Convert DataFrame → list of dicts (VERY IMPORTANT for bulk)
        records = df.to_dict(orient="records")

        # Bulk UPSERT
        conn.execute(text(f"""
            INSERT INTO {table_name} (
                medicine_id, name, price, is_discontinued, manufacturer, type, pack_size,
                short_com_1, short_com_2, salt_composition, medicine_name,
                side_effects, drug_interactions
            ) VALUES (
                :medicine_id, :name, :price, :is_discontinued, :manufacturer, :type, :pack_size,
                :short_com_1, :short_com_2, :salt_composition, :medicine_name,
                :side_effects, :drug_interactions
            )
            ON DUPLICATE KEY UPDATE
                name = VALUES(name),
                price = VALUES(price),
                is_discontinued = VALUES(is_discontinued),
                manufacturer = VALUES(manufacturer),
                type = VALUES(type),
                pack_size = VALUES(pack_size),
                short_com_1 = VALUES(short_com_1),
                short_com_2 = VALUES(short_com_2),
                salt_composition = VALUES(salt_composition),
                medicine_name = VALUES(medicine_name),
                side_effects = VALUES(side_effects),
                drug_interactions = VALUES(drug_interactions)
        """), records)

    print(f"🚀 Bulk upsert completed: {len(df)} medicines loaded")
