import streamlit as st 
import pandas as pd 
from app.data_loader import load_data 
from app.analyzer import get_top_products, get_revenue_by_month 
import matplotlib.pyplot as plt 

df = load_data("data/mock_orders.csv")

st.sidebar.title("Filters")
selected_country = st.sidebar.multiselect("Country", df['country'].unique(), default = df['country'].unique())

filtered_df = df[df['country'].isin(selected_country)]


st.title("eCommerce Dashboard")

st.subheader("Top Selling Products")
top_products = get_top_products(filtered_df)
st.dataframe(top_products)

total_revenue = filtered_df["total_price"].sum()
total_orders = filtered_df["order_id"].nunique()
aov = total_revenue / total_orders if total_orders > 0 else 0

st.metric(label = "Average Order Value (AOV)", value = f"${aov:.2f}")

st.subheader("AOV by Country")
aov_by_country = (
    filtered_df.groupby("country")
    .apply(lambda x: x["total_price"].sum() / x["order_id"].nunique())
    .sort_values(ascending = False)
)
st.bar_chart(aov_by_country)

st.subheader("Monthly Revenue Trend")
revenue = get_revenue_by_month(filtered_df)

fig, ax = plt.subplots()
revenue.plot(marker = 'o', ax = ax)
ax.set_title("Revenue Over Time")
ax.set_xlabel("Month")
ax.set_ylabel("Total Revenue")
ax.grid(True)
st.pyplot(fig)

st.subheader("Sales by Country")
country_sales = (
    filtered_df.groupby("country")["total_price"]
    .sum()
    .sort_values(ascending = False)

)
st.bar_chart(country_sales)

st.subheader("Sales by Category")

category_sales = (
    filtered_df.groupby("category")["total_price"]
    .sum()
    .sort_values(ascending = False)
)

fig2, ax2 = plt.subplots()
ax2.pie(category_sales, labels = category_sales.index, autopct = '%1.1f%%', startangle = 90)
ax2.axis('equal')
st.pyplot(fig2)


st.subheader("Sales by Day of Week")

filtered_df["order_date"] = pd.to_datetime(filtered_df["order_date"])

filtered_df["day_of_week"] = filtered_df["order_date"].dt.day_name()

sales_by_day = (
    filtered_df.groupby("day_of_week")["total_price"]
    .sum()
    .reindex([
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ])
)

st.bar_chart(sales_by_day)


