import matplotlib.pyplot as plt 

def plot_revenue_trend(revenue_series):
    plt.figure(figsize = (8, 4))
    revenue_series.plot(marker = 'o')
    plt.title("Monthly Revenue Trend")
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.grid(True)
    plt.tight_layout()
    plt.show()