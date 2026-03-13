import pyodbc
import pandas as pd

from utils.logger import setup_logger
from config.config import Config

logger = setup_logger(__name__)


def get_weather_data(query: str):

    connection_string = (
        f"DRIVER={{{Config.DB_DRIVER}}};"
        f"SERVER={Config.DB_SERVER};"
        f"DATABASE={Config.DB_DATABASE};"
        f"UID={Config.DB_USER};"
        f"PWD={Config.DB_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )

    try:
        logger.info("Подключение к базе данных")

        connection = pyodbc.connect(connection_string)

        df = pd.read_sql_query(query, connection)

        logger.info("Данные успешно загружены")

        return df

    except Exception as e:

        logger.error(f"Ошибка подключения: {e}")

        return None

    finally:

        if 'connection' in locals() and connection:
            connection.close()
            logger.info("Соединение с базой закрыто")