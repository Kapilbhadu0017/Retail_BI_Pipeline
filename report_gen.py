import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import os

conn = sqlite3.connect('data/retail.db')
os.makedirs('reports/charts', exist_ok = True)

q1 = pd.read_sql_query("""
    SELECT region, 
        ROUND(SUM(sales), 2) as total_revenue,
        ROUND(SUM(profit), 2) as total_profit
    FROM sales
    GROUP BY region
    ORDER BY total_revenue ASC
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

# Chart 1: Revenue by Region
plt.figure(figsize=(10, 6))
plt.barh(q1['region'], q1['total_revenue'])
plt.xlabel('Total Revenue ($)')
plt.ylabel('Region')
plt.title('Total Revenue by Region')
plt.tight_layout()
plt.savefig('reports/charts/revenue_by_region.png', bbox_inches='tight')
plt.close()

# chart 2:top 10 profitable products
plt.figure(figsize=(10,6))
plt.barh(q2['product_name'].iloc[::-1], q2['total_profit'].iloc[::-1])
plt.xlabel('Total Profit')
plt.ylabel('Product Name')
plt.title("Top 10 Most Profitable Products")
plt.tight_layout()
plt.savefig('reports/charts/top_products.png', bbox_inches='tight')
plt.close()

# chart 3: Monthly Sales Trend
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14,5))
sns.lineplot(data=q3, x='month', y='monthly_revenue', marker='o', color='#1f77b4', linewidth=2.5)
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.savefig('reports/charts/monthly_trend.png', bbox_inches='tight')
plt.close()











# print(q1)
# print(q2)
# print(q3.head(5))
# print(q4)
# print(q5)