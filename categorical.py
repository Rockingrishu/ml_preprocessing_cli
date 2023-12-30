import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from data_description import DataDescription
from logging_and_reporting import LoggingAndReporting

class Categorical:
    # The Task associated with this class.
    tasks = [
        '\n1. Show Categorical Columns',
        '2. Performing One Hot encoding',
        '3. Performing Binary encoding',
        '4. Performing Label encoding',
        '5. Show the Dataset'
    ]

    def __init__(self, data):
        self.data = data

    # function to show all the categorical columns and number of unique values in them.
    def categoricalColumn(self):
        print('\n{0: <20}'.format("Categorical Column") + '{0: <5}'.format("Unique Values"))
        # select_dtypes selects the columns with object datatype(which could be further categorized)
        for column in self.data.select_dtypes(include="object"):
            print('{0: <20}'.format(column) + '{0: <5}'.format(self.data[column].nunique()))

    # function to encode any particular column with one-hot encoding
    def oneHotEncoding(self, column):
        self.data = pd.get_dummies(data=self.data, columns=[column])
        print(f"One-Hot Encoding for {column} is done...\U0001F601")

    # function to encode any particular column with binary encoding
    def binaryEncoding(self, column):
        binary_encoder = LabelEncoder()
        self.data[column] = binary_encoder.fit_transform(self.data[column])
        print(f"Binary Encoding for {column} is done...\U0001F601")

    # function to encode any particular column with label encoding
    def labelEncoding(self, column):
        label_encoder = LabelEncoder()
        self.data[column] = label_encoder.fit_transform(self.data[column])
        print(f"Label Encoding for {column} is done...\U0001F601")

    # The main function of the Categorical class.
    def categoricalMain(self):
        LoggingAndReporting(self.data, self.data).log_preprocessing_step("Data Description", {})

        while True:
            print("\nTasks\U0001F447")
            for task in self.tasks:
                print(task)

            while True:
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required. Try again...\U0001F974")
                    continue
                break

            if choice == -1:
                break

            elif choice == 1:
                self.categoricalColumn()

            elif choice == 2:
                self.categoricalColumn()
                column = input("\nWhich column would you like to one-hot encode? ")
                if column in self.data.select_dtypes(include="object"):
                    self.oneHotEncoding(column)
                else:
                    print("Invalid column name. Please try again...\U0001F974")

            elif choice == 3:
                self.categoricalColumn()
                column = input("\nWhich column would you like to binary encode? ")
                if column in self.data.select_dtypes(include="object"):
                    self.binaryEncoding(column)
                else:
                    print("Invalid column name. Please try again...\U0001F974")

            elif choice == 4:
                self.categoricalColumn()
                column = input("\nWhich column would you like to label encode? ")
                if column in self.data.select_dtypes(include="object"):
                    self.labelEncoding(column)
                else:
                    print("Invalid column name. Please try again...\U0001F974")

            elif choice == 5:
                DataDescription.showDataset(self)

            else:
                print("\nWrong Integer value!! Try again..\U0001F974")

        # return the data after modifying
        return self.data


