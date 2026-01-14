import urllib
from sqlalchemy import create_engine
import os 

def connect():
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