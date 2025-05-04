from app.data_loader import load_data
from app.analyzer import get_top_products, get_revenue_by_month
from app.visualizer import plot_revenue_trend


if __name__ == "__main__":
    df = load_data("data/mock_orders.csv")

    print("Top Products :")
    print(get_top_products(df))


    revenue = get_revenue_by_month(df)
    plot_revenue_trend(revenue)
