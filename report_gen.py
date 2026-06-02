import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 
import os

conn = sqlite3.connect('data/retail.db')
os.makedirs('reports/charts', exist_ok = True)

q1 = pd.read_sql_query("""
    SELECT region, 
        ROUND(SUM(sales), 2) as total_revenue,
        ROUND(SUM(profit), 2) as total_profit
    FROM sales
    GROUP BY region
    ORDER BY total_revenue DESC
""", conn)

q2 = pd.read_sql_query("""
    SELECT product_name,
        ROUND(SUM(profit), 2) as total_profit
    FROM SALES
    GROUP BY product_name
    ORDER BY total_profit DESC
    LIMIT 10
""", conn)

q3 = pd.read_sql_query("""
    SELECT STRFTIME('%Y-%m', order_date) AS month,
        ROUND(SUM(sales), 2) as monthly_revenue
    FROM sales
    GROUP BY month
    ORDER BY month
""", conn)

q4 = pd.read_sql_query("""
    select category,
        round(sum(sales),2) as total_sales,
        round(sum(profit),2) as total_profit,
        round((sum(profit) / sum(sales)*100), 2) as profit_margin_pct
    from sales
    group by category
    order by profit_margin_pct desc
""", conn)

q5 = pd.read_sql_query("""
    select round(discount, 1) as discount_level,
        round(avg(profit), 2) avg_profit,
        count(*) as num_orders
    from sales
    group by discount_level
    order by discount_level
""", conn)

conn.close()

print(q1)
print(q2)
print(q3.head(5))
print(q4)
print(q5)