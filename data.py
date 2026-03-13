
import pyodbc
import pandas as pd

def get_weather_data(query):
    server = 'RICCO\SQLEXPRESS'  # Замените на имя вашего сервера
    database = 'WeatherDB'  # Замените на название базы данных
    driver = '{ODBC Driver 17 for SQL Server}'  # Убедитесь, что ODBC драйвер установлен
    uid = 'sa'
    pwd = 'Dialog1996'

    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};" \
                        f"UID={uid};PWD={pwd};TrustServerCertificate=yes;" \
      #                  f"Trusted_Connection=yes;"
    #connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

    try:
        connection = pyodbc.connect(connection_string)
        print("Подключение успешно")

        # Выполнение запроса и загрузка данных в DataFrame
        df = pd.read_sql_query(query, connection)
        return df

    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

    finally:
        # Закрытие соединения
        if 'connection' in locals() and connection:
            connection.close()
            print("Соединение закрыто")
