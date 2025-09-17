# SimStockTempDB

SimStockTempDB is a full-stack trading simulation platform designed for educational and research purposes. It provides real-time and historical stock data visualization, simulates trading activities, and demonstrates database management for financial applications.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

SimStockTempDB enables users to view live and historical stock data, interact with simulated trading environments, and analyze market trends. The project consists of a React-based frontend and a FastAPI-powered backend connected to a PostgreSQL database.

## Features

- **Live Stock Charting:** Real-time candlestick and volume charts for selected companies.
- **Company List:** Easily switch between major companies (Apple, Microsoft, IBM, Google, Tesla, etc.).
- **Historical Data Simulation:** Backend scripts to simulate and insert historical trading data.
- **RESTful API:** FastAPI endpoints for fetching stock data and managing trading simulations.
- **Modern UI:** Responsive dashboard built with React, Tailwind CSS, and Flowbite.
- **Database Integration:** PostgreSQL for robust data storage and aggregation.

## Architecture

```
SimStockTempDB/
├── backend/
│   ├── main.py            # FastAPI server and API endpoints
│   ├── fetch.py           # Fetches and aggregates minute-level data
│   ├── simulate.py        # Simulates historical data insertion
│   ├── test.py            # Test script for database operations
│   ├── historical_data.csv# Sample historical data
├── frontend/
│   ├── src/
│   │   ├── components/    # React components (Dashboard, Livechart, Companylist, etc.)
│   │   ├── data/          # Company list, chart options, data services
│   ├── public/            # Static assets and index.html
│   ├── package.json       # Frontend dependencies
├── README.md              # Project documentation
```

## Technologies Used

- **Frontend:** React, Tailwind CSS, Flowbite, ApexCharts
- **Backend:** FastAPI, psycopg2, pandas
- **Database:** PostgreSQL
- **Other:** Day.js, Lightweight Charts

## Setup Instructions

### Backend

1. Install Python dependencies:
   ```bash
   pip install fastapi psycopg2 pandas
   ```
2. Set up PostgreSQL and create the required tables (`minuteaggregateddata`, `companydata`, etc.).
3. Run the backend server:
   ```bash
   python backend/main.py
   ```

### Frontend

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install Node.js dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
   The app will be available at [http://localhost:3000](http://localhost:3000).

## Usage

- Access the dashboard to view live and historical stock charts.
- Select companies from the dropdown to switch views.
- Backend endpoints provide data for frontend visualization and can be extended for trading logic.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License

This project is for educational purposes.

