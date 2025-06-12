# Create a SQLite database file with just one sales table
import sqlite3
import pandas as pd 

df = pd.read_excel('data/Pizza_Sales.xlsx')

conn = sqlite3.connect('data/Pizza_Sales.db')
df.to_sql('sales', conn, if_exists='replace', index=False)

print("✅ Database 'pizza_sales.db' created and data inserted into 'sales' table.")

conn.close()
