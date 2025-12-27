# 💊 Medicine ETL Pipeline

A modular data engineering project that extracts medicine data from CSVs, cleans it, and loads it into a MySQL database. Designed with a production-ready folder structure and connection testing.

<img width="457" height="530" alt="image" src="https://github.com/user-attachments/assets/4fbeb4dc-5f57-483d-9810-e32f9c6b45c6" />




## 📂 Project Structure

medicine-etl-pipleine/
├── data/
│   └── sample_clinicaltrials.csv  # Raw source data
├── sql/
│   ├── schema.sql                 # Table definitions
│   └── sample_queries.sql         # SQL for analysis
├── src/
│   ├── db.py                      # Database connection factory
│   ├── extract.py                 # Data extraction logic
│   ├── transform.py               # Data cleaning & normalization
│   ├── load.py                    # Bulk database loading
│   ├── pipeline.py                # Main orchestration script
│   └── test_db.py                 # Connection verification script
└── README.md


## 🚀 Features
- **Modular Design**: Separate logic for Extract, Transform, and Load steps.
- **Connection Testing**: Includes `test_db.py` to verify database connectivity before running heavy jobs.
- **Data Quality**: Handles missing values and schema validation automatically.

## 🛠️ Tech Stack
- **Python 3**: Core programming language.
- **MySQL Workbench**: Database design and management.
- **SQLAlchemy**: ORM for database connections.
- **Pandas**: High-performance data manipulation.

## ⚙️ Setup & Run
1. **Configure Database**:
   - Create the schema using `sql/schema.sql` in MySQL Workbench.
   - Update credentials in `src/db.py`.

2. **Verify Connection**:
python src/test_db.py

Output: ('pharma_dw',) -> Success!

3. **Run Pipeline**:
python src/pipeline.py
