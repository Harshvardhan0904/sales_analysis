import pandas as pd
import urllib
from sqlalchemy import create_engine
import os 

def get_engine():
    SERVER = 'server_name'
    DATABASE = 'db_name'
    USERNAME = 'u_name'
    PASSWORD = 'pwd'
    DRIVER = '{ODBC Driver 18 for SQL Server}'
    connection_string = (
        f"Driver={DRIVER};"
        f"Server=tcp:{SERVER},1433;"
        f"Database={DATABASE};"
        f"Uid={USERNAME};"
        f"Pwd={PASSWORD};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
        f"Connection Timeout=30;"
    )
    params = urllib.parse.quote_plus(connection_string)
    engine_url = f"mssql+pyodbc:///?odbc_connect={params}"
    return create_engine(engine_url, fast_executemany=True)

def ingest_csv_to_azure(csv_file, table_name, chunksize=10000):
    engine = get_engine()
    for chunk in pd.read_csv(csv_file, chunksize=chunksize):
        chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists='append',  
            index=False,
            chunksize=1000       
        )
        print(f'{len(chunk)} rows uploaded')


for file in os.listdir('data'):
    csv_file = os.path.join('data',file)
    ingest_csv_to_azure(csv_file, table_name='vendor_invoice')
