import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up database connection
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

# Define path
csv_path = "data/mlb_pitch_data_2024.csv"

try:
    print("[INFO] Reading CSV...")
    df = pd.read_csv(csv_path)
    print(f"[INFO] Loaded {len(df):,} rows and {len(df.columns)} columns.")

    # Clean column names for PostgreSQL compatibility
    df.columns = df.columns.str.replace(r'\W+', '_', regex=True)
    df.columns = df.columns.str.lower()
    print("[INFO] Column names cleaned.")

    print("[INFO] Starting upload to RDS...")
    df.to_sql("pitch_data", con=engine, if_exists="replace", index=False, chunksize=1000, method='multi')
    print("[SUCCESS] Upload complete!")

except SQLAlchemyError as e:
    print("[ERROR] SQLAlchemy error during upload:", str(e.__cause__))
except Exception as e:
    print("[ERROR] General error:", e)



