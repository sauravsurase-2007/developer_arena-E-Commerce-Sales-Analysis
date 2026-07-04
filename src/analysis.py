import pandas as pd


class DataAnalysis:

    def __init__(self, data):
        self.data = data

    def total_sales(self):
        total = self.data["Sales"].sum()
        print(f"\nTotal Sales : ₹{total}")

    def average_sales(self):
        avg = self.data["Sales"].mean()
        print(f"Average Sales : ₹{avg:.2f}")

    def highest_sale(self):
        highest = self.data.loc[self.data["Sales"].idxmax()]
        print("\nHighest Sale")
        print(highest)

    def lowest_sale(self):
        lowest = self.data.loc[self.data["Sales"].idxmin()]
        print("\nLowest Sale")
        print(lowest)

    def sales_by_category(self):
        return self.data.groupby("Category")["Sales"].sum()

    def monthly_sales(self):
        self.data["Date"] = pd.to_datetime(self.data["Date"])
        self.data["Month"] = self.data["Date"].dt.strftime("%B")
        return self.data.groupby("Month")["Sales"].sum()

    def sales_distribution(self):
        return self.data.groupby("Category")["Sales"].sum()
        