import psycopg2
import time
from datetime import datetime

# Database connection parameters
DB_NAME = "DBMS Term Project"
DB_USER = "postgres"
DB_PASSWORD = "Ajay@123"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to the database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

# Initialize variable to store last minute
last_minute = None

try:
    while True:
        # Get current time
        current_time = datetime.now()

        # Extract minute from current time
        current_minute = current_time.minute
        
        current_time_truncated = current_time.replace(second=0, microsecond=0)
        if current_minute != last_minute:
            # Fetch aggregated data for the new minute from the database
            print("SELECT * FROM minuteaggregateddata WHERE minute_start = %s" % current_time_truncated)
            cur.execute("SELECT * FROM minuteaggregateddata WHERE minute_start = %s", (current_time_truncated,))
            row = cur.fetchone()

            # Display OHLCV values for the new minute
            if row:
                print("Minute:", current_time.strftime("%Y-%m-%d %H:%M"))
                print("Open:", row[1])
                print("High:", row[2])
                print("Low:", row[3])
                print("Close:", row[4])
                print("Volume:", row[5])
                print("---------------------------------------")

            # Update last minute
            last_minute = current_minute

        # Sleep for one second
        time.sleep(1)

except KeyboardInterrupt:
    # Close database connection
    conn.close()

