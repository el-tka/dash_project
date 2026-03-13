import pyodbc
import pandas as pd

from utils.config import Config


def get_connection():

    connection_string = (
        f"DRIVER={{{Config.DB_DRIVER}}};"
        f"SERVER={Config.DB_SERVER};"
        f"DATABASE={Config.DB_DATABASE};"
        f"UID={Config.DB_USER};"
        f"PWD={Config.DB_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )

    connection = pyodbc.connect(connection_string)

    return connection


def get_weather_data(query: str) -> pd.DataFrame:

    connection = None

    try:
        connection = get_connection()

        df = pd.read_sql_query(query, connection)

        return df

    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

    finally:
        if connection:
            connection.close()