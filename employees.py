import pandas as pd

class EmployeeDataLoader:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.employee_data = None

    def load_data(self):
        try:
            # Read CSV file into a Pandas DataFrame
            self.employee_data = pd.read_csv(self.csv_file)
            print("Employee data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File '{self.csv_file}' not found.")
        except pd.errors.EmptyDataError:
            print(f"Error: File '{self.csv_file}' is empty.")
        except pd.errors.ParserError:
            print(f"Error: Unable to parse data from '{self.csv_file}'. Check the file format.")

    def display_data(self):
        if self.employee_data is not None:
            # Display the loaded data
            print(self.employee_data)
        else:
            print("Error: No data loaded. Use 'load_data()' method first.")

# Example usage
csv_file_path = 'employee_data.csv'  # Replace with your CSV file path
employee_loader = EmployeeDataLoader(csv_file_path)

# Load data from the CSV file
employee_loader.load_data()

# Display the loaded data
employee_loader.display_data()
