import sqlite3
import pandas as pd

df = pd.read_csv('data/clean/clean.csv', parse_dates=['order_date', 'ship_date'])

conn = sqlite3.connect('data/retail.db')

df.to_sql('sales', conn, if_exists='replace', index=False)

cursor = conn.cursor()
cursor.execute('select count(*) from sales')

print('Total Rows:',cursor.fetchone()[0])

conn.close()