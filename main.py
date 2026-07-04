from src.data_loader import DataLoader
from src.analysis import DataAnalysis
from src.visualization import Visualizer
from src.utils import create_folders, heading


def main():

    create_folders()

    heading("E-COMMERCE SALES ANALYSIS PROJECT")

    loader = DataLoader("data/sales_data.csv")

    data = loader.load_data()

    if data is None:
        return

    loader.dataset_info()

    loader.show_first_rows()

    loader.missing_values()

    loader.clean_data()

    analysis = DataAnalysis(data)

    analysis.total_sales()

    analysis.average_sales()

    analysis.highest_sale()

    analysis.lowest_sale()

    visual = Visualizer()

    category_sales = analysis.sales_by_category()

    monthly_sales = analysis.monthly_sales()

    distribution = analysis.sales_distribution()

    visual.bar_chart(category_sales)

    visual.line_chart(monthly_sales)

    visual.pie_chart(distribution)

    print("\n=================================")
    print("Project Completed Successfully")
    print("Charts saved in visualizations/")
    print("=================================")


if __name__ == "__main__":
    main()