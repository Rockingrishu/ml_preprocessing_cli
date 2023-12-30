import pandas as pd
from logging_and_reporting import LoggingAndReporting

class DataDescription:
    # The Task associated with this class.
    tasks = [
        '\n1. Describe a specific Column',
        '2. Show Properties of Each Column',
        '3. Show the Dataset',
        '4. Delete columns with single values',
        '5. Delete columns with more than 50% null values',
        '6. Delete duplicate rows',
        '7. Show Missing Values'
    ]

    def __init__(self, data):
        self.data = data

    def showDataset(self):
        while True:
            try:
                rows = int(input("\nHow many rows(>0) to print? (Press -1 to go back)  "))
                if rows == -1:
                    break
                if rows <= 0:
                    print("Number of rows given must be +ve...\U0001F974")
                    continue
                print(self.data.head(rows))
            except ValueError:
                print("Numeric value is required. Try again....\U0001F974")
                continue
            break

    # function to print all the columns
    def showColumns(self):
        for column in self.data.columns.values:
            print(column, end="  ")

    # function to describe the dataset or any specific column.
    def describe(self):
        LoggingAndReporting(self.data, self.data).log_preprocessing_step("Data Description", {})

        while True:
            print("\nTasks (Data Description)\U0001F447")
            for task in self.tasks:
                print(task)

            while True:
                try:
                    choice = int(input("\n\nWhat you want to do? (Press -1 to go back)  "))
                except ValueError:
                    print("Integer Value required. Try again.....\U0001F974")
                    continue
                break

            if choice == -1:
                break

            elif choice == 1:
                self.showColumns()
                while True:
                    describeColumn = input("\n\nWhich Column?  ").lower()
                    try:
                        # describe() function is used to tell all the info regarding any specific column.
                        print(self.data[describeColumn].describe())
                    except KeyError:
                        print("No Column present with this name. Try again....\U0001F974")
                        continue
                    break

            elif choice == 2:
                # describe() function is used to tell all the info about the database.
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())

            elif choice == 3:
                self.showDataset()

            elif choice == 4:
                self.deleteSingleValueColumns()

            elif choice == 5:
                self.deleteColumnsWithNullValues()

            elif choice == 6:
              self.deleteDuplicateRows()

            elif choice == 7:
                self.showMissingValues()

            else:
                print("\nWrong Integer value!! Try again..\U0001F974")

    def deleteSingleValueColumns(self):
        # Identify columns with a single unique value
        single_value_columns = [col for col in self.data.columns if self.data[col].nunique() == 1]

        # Delete identified columns
        if single_value_columns:
            self.data.drop(columns=single_value_columns, inplace=True)
            print("Columns with single values deleted successfully.")
        else:
            print("No columns with single values found.")

    def deleteColumnsWithNullValues(self):
        # Identify columns with more than 50% null values
        null_percentage_threshold = 50.0
        null_percentage = (self.data.isnull().sum() / len(self.data)) * 100
        columns_with_null_values = null_percentage[null_percentage > null_percentage_threshold].index.tolist()

        # Delete identified columns
        if columns_with_null_values:
            self.data.drop(columns=columns_with_null_values, inplace=True)
            print("Columns with more than 50% null values deleted successfully.")
        else:
            print("No columns with more than 50% null values found.")


    def deleteDuplicateRows(self):
        # Identify and delete duplicate rows
        initial_rows = len(self.data)
        self.data.drop_duplicates(inplace=True)
        final_rows = len(self.data)

        if initial_rows != final_rows:
            print(f"{initial_rows - final_rows} duplicate rows deleted successfully.")
        else:
            print("No duplicate rows found.")

    def showMissingValues(self):
        # Show missing values in the dataset
        missing_values = self.data.isnull().sum()
        print("Missing Values:\n", missing_values)