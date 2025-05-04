def get_top_products(df, n = 5):
    return df.groupby('product_name')['total_price'].sum().sort_values(ascending = False). head(n)

def get_revenue_by_month(df):
    return df.set_index('order_date').resample('M')['total_price'].sum()