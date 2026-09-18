import pandas as pd
import matplotlib.pyplot as plt
import os

# Load sales data
data = pd.read_excel("sales_data.xlsx")

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Dataset preview
print("\n--- Dataset Preview ---")
print(data.head())

# Statistical summary
print("\n--- Statistical Summary ---")
print(data.describe())

# Top 5 sales
top_sales = data.sort_values("Sales_Amount", ascending=False)

print("\n--- Top 5 Sales ---")
print(top_sales[["Product", "Sales_Amount", "Profit"]].head())

# Region-wise sales
region_sales = data.groupby("Region")["Sales_Amount"].sum()

print("\n--- Region-wise Sales ---")
print(region_sales)

# Product-wise profit
product_profit = data.groupby("Product")["Profit"].sum()

print("\n--- Product-wise Profit ---")
print(product_profit)

# Region-wise Sales Chart
region_sales.plot(kind="bar")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.title("Region-wise Sales Analysis")
plt.tight_layout()
plt.savefig("outputs/region_sales.png")
plt.show()
plt.close()

# Sales vs Profit Chart
plt.scatter(data["Sales_Amount"], data["Profit"])
plt.xlabel("Sales Amount")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.tight_layout()
plt.savefig("outputs/sales_vs_profit.png")
plt.show()
plt.close()

print("\nAnalysis completed successfully!")
