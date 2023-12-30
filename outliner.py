
# outliners.py

class Outliners:
    def __init__(self, data):
        self.data = data

    def detect_and_remove_outliers(self):
        # Implement your outlier detection and removal logic here
        # For example, you can use Z-score or IQR methods

        # Assume 'numeric_columns' contains the names of numeric columns in your dataset
        numeric_columns = self.data.select_dtypes(include=['float64', 'int64']).columns

        for column in numeric_columns:
            # Calculate Z-scores for each data point in the column
            z_scores = (self.data[column] - self.data[column].mean()) / self.data[column].std()

            # Define a threshold for Z-score to identify outliers (you can adjust this threshold)
            outlier_threshold = 3

            # Identify and remove outliers
            self.data = self.data[abs(z_scores) < outlier_threshold]

        print("Outliers removed successfully...\U0001F44C")
        return self.data
