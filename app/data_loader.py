import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates = ['order_date'])
    df['total_price'] = df['quantity'] * df['unit_price']
    return df