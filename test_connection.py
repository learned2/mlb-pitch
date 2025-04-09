from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get credentials
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Create SQLAlchemy engine
connection_string = f"postgresql://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(connection_string)

# Test connection
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("Connection successful!")
        print(result.fetchone())
except Exception as e:
    print("Connection failed:", e)
