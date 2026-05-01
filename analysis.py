import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("sales_data.xlsx")

print(data.head())
print(data.describe())

top_sales = data.sort_values("Sales_Amount", ascending=False)
print(top_sales.head())

region_sales = data.groupby("Region")["Sales_Amount"].sum()
print(region_sales)

region_sales.plot(kind="bar")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.title("Region-wise Sales Analysis")
plt.show()

plt.scatter(data["Sales_Amount"], data["Profit"])
plt.xlabel("Sales Amount")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.show()
