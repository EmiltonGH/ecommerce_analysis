import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates = ['date'])
    df['total_price'] = df['quantity'] * df['price_per_unit']
    return df