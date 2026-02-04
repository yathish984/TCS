


# Machine Learning Financial Analysis Project

## Project Overview
This project fetches financial data (Balance Sheet, Profit & Loss, Cash Flow) from a StockTicker API,
applies machine learning based rule analysis to generate pros and cons,
and stores the results in a MySQL database.
The output is displayed in the terminal and on a web interface.

## Tech Stack
- Python
- Pandas
- Requests
- SQLAlchemy
- MySQL
- VS Code

## Data Source
API Endpoint:
https://bluemutualfund.in/server/api/company.php

## Project Workflow
1. Read company symbols from CSV
2. Fetch financial data using API
3. Analyze data to generate Pros & Cons
4. Store analysis in MySQL
5. Display results in terminal and web app

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Create MySQL database and table:
   CREATE DATABASE ml_financial;

3. Run the project:
   python main.py

## Output
- Terminal displays financial pros and cons
- Data stored in MySQL table
- Web page shows company analysis
