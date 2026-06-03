import pandas as pd

df = pd.read_csv('data/raw/Sample - Superstore.csv',encoding='latin-1')

df.drop_duplicates()

for col in df.columns:
    if df[col].dtype == 'str':
        df[col] = df[col].str.strip()

pd.set_option('display.max_columns', None)

new_header = list(df.columns)

for i in range(len(new_header)):
    new_header[i] = new_header[i].lower()
    new_header[i] = new_header[i].strip()
    new_header[i] = new_header[i].replace(' ','_').replace('-','_')

df.columns = new_header

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

df.to_csv('data/clean/clean.csv', index = False)

