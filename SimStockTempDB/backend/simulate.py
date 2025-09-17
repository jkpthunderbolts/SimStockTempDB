import pandas as pd
import psycopg2
import time
from datetime import datetime

# Database connection parameters
DB_NAME = "DBMS Term Project"
DB_USER = "postgres"
DB_PASSWORD = "Ajay@123"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    # Connect to the database
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()
    historical_df = pd.read_csv('historical_data.csv', index_col=0)
    print(historical_df.head())
    for index, row in historical_df.iterrows():
        timestamp = datetime.now().replace(microsecond=0)
        price = row["Price"]
        volume = row["Volume"]
        cur.execute(
            "INSERT INTO companydata (timestamp, price, day_volume) VALUES (%s, %s, %s)",
            (timestamp, price, volume),
        )
        conn.commit()

        print("Inserted data at:", timestamp)
        time.sleep(1)

except (psycopg2.Error, KeyboardInterrupt) as error:
    print("Error:", error)

finally:
    # Close database connection
    if 'conn' in locals():
        conn.close()
