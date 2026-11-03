from sqlalchemy import create_engine  # type: ignore
from dotenv import load_dotenv     # type: ignore 
import os
import pandas as pd # type: ignore

df = pd.read_csv(r'customer_cleaned.csv')

load_dotenv()

db_url = os.getenv("SQL_DB_URL")

engine = create_engine(db_url, echo=False)

table_name = "customer_data"

df.to_sql(table_name, engine, if_exists='replace', index=False)