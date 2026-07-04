import pandas as pd


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Load CSV file"""
        try:
            self.data = pd.read_csv(self.file_path)
            print("✅ Dataset Loaded Successfully")
            return self.data

        except FileNotFoundError:
            print("❌ File not found.")
            return None

        except Exception as e:
            print("Error:", e)
            return None

    def dataset_info(self):
        """Display dataset information"""
        if self.data is not None:
            print("\n========== Dataset Info ==========")
            print(self.data.info())

    def show_first_rows(self):
        """Display first 5 rows"""
        if self.data is not None:
            print("\n========== First 5 Rows ==========")
            print(self.data.head())

    def missing_values(self):
        """Display missing values"""
        if self.data is not None:
            print("\n========== Missing Values ==========")
            print(self.data.isnull().sum())

    def clean_data(self):
        """Remove duplicate values"""
        if self.data is not None:
            self.data.drop_duplicates(inplace=True)
            self.data.fillna(0, inplace=True)
            print("✅ Data Cleaned Successfully")