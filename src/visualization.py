import matplotlib.pyplot as plt
import os


class Visualizer:

    def __init__(self):
        os.makedirs("visualizations", exist_ok=True)

    def bar_chart(self, data):

        plt.figure(figsize=(8,5))

        data.plot(kind="bar")

        plt.title("Sales by Category")

        plt.xlabel("Category")

        plt.ylabel("Sales")

        plt.tight_layout()

        plt.savefig("visualizations/sales_by_category.png")

        plt.close()

        print("✅ Bar Chart Saved")

    def line_chart(self, data):

        plt.figure(figsize=(8,5))

        data.plot(kind="line", marker="o")

        plt.title("Monthly Sales")

        plt.xlabel("Month")

        plt.ylabel("Sales")

        plt.tight_layout()

        plt.savefig("visualizations/monthly_sales.png")

        plt.close()

        print("✅ Line Chart Saved")

    def pie_chart(self, data):

        plt.figure(figsize=(7,7))

        data.plot(kind="pie", autopct="%1.1f%%")

        plt.ylabel("")

        plt.title("Sales Distribution")

        plt.tight_layout()

        plt.savefig("visualizations/sales_distribution.png")

        plt.close()

        print("✅ Pie Chart Saved")