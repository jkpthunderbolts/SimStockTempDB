import psycopg2
import time
from datetime import datetime
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import json

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
if conn:
    print("Database connected")
    
    

app = FastAPI()
cors = CORSMiddleware(app, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/stock_data_candle")
def read_stock_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM minuteaggregateddata;")
    rows = cur.fetchall()
    stockdata = []
    for i in range(len(rows)):
        stockdata.append([rows[i][0].strftime("%Y-%m-%d %H:%M:00"), rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5],])
    return stockdata

@app.get("/stock_data_price_timerange")
def read_stock_data_price_timerange(start: str, end: str):
    cur = conn.cursor()
    cur.execute("SELECT * FROM minuteaggregateddata WHERE timestamp >= %s AND timestamp <= %s;", (start, end))
    rows = cur.fetchall()
    stockdata = []
    for row in rows:
        stockdata.append([row[0].strftime("%Y-%m-%d %H:%M:00"), row[1], row[2], row[3], row[4], row[5]])
    return stockdata

@app.get("/moving_average")
def read_moving_average():
    cur = conn.cursor()
    cur.execute("SELECT * FROM fiveminutemovingaverage;")
    rows = cur.fetchall()
    movingaverage = []
    for row in rows:
        movingaverage.append([row[0].strftime("%Y-%m-%d %H:%M:00"), row[1]])
    return movingaverage

@app.get("/bollinger_bands")
def read_bollinger_bands():
    cur = conn.cursor()
    cur.execute("SELECT * FROM bollingerbands;")
    rows = cur.fetchall()
    bollingerbands = []
    for row in rows:
        bollingerbands.append([row[0].strftime("%Y-%m-%d %H:%M:00"), row[1], row[2],row[3]])
    return bollingerbands

@app.get("/accudist")
def read_accudist():
    cur = conn.cursor()
    cur.execute("SELECT * FROM accumulationdistribution;")
    rows = cur.fetchall()
    accudist = []
    for row in rows:
        accudist.append([row[0].strftime("%Y-%m-%d %H:%M:00"), row[1]])
    return accudist

@app.get("/rsi")
def read_rsi():
    cur = conn.cursor()
    cur.execute("SELECT * FROM rsi;")
    rows = cur.fetchall()
    rsi = []
    for row in rows:
        rsi.append([row[0].strftime("%Y-%m-%d %H:%M:00"), row[1]])
    return rsi

@app.get("/macd")
def read_macd():
    cur = conn.cursor()
    cur.execute("SELECT * FROM twentysixminuteema;")
    rows = cur.fetchall()
    cur.execute("SELECT * FROM twelveminuteema;")
    rows2 = cur.fetchall()
    macd = []
    for i in range(len(rows)):
        macd.append([rows[i][0].strftime("%Y-%m-%d %H:%M:00"), rows[i][1] - rows2[i][1]])
    return macd

@app.get("/twelveminuteema")
def read_twelveminuteema():
    cur = conn.cursor()
    cur.execute("SELECT * FROM twelveminuteema;")
    rows = cur.fetchall()
    twelveminuteema = []
    for row in rows:
        twelveminuteema.append([row[0].strftime("%Y-%m-%d %H:%M:00"), row[1]])
    return twelveminuteema