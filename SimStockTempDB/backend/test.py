import psycopg2
import time
from datetime import datetime

# Database connection parameters
DB_NAME = "trading"
DB_USER = "postgres"
DB_PASSWORD = "Ajay@123"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to the database
conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
)
cur = conn.cursor()

# Main loop to insert data every second
try:
    x = 0
    while True:
        timestamp = datetime.now()

        # Generate dummy data for price and day_volume (replace with your actual data)
        price = 100.0 + x  # Example price
        day_volume = 1000  # Example day volume

        # Insert data into the CompanyData table
        cur.execute(
            "INSERT INTO CompanyData (timestamp, price, day_volume) VALUES (%s, %s, %s)",
            (timestamp, price, day_volume),
        )
        conn.commit()

        print("Inserted data at:", timestamp)
        x += 1
        time.sleep(1)

except KeyboardInterrupt:
    # Close database connection
    conn.close()

