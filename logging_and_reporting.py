# logging_and_reporting.py

import logging
import pandas as pd

class LoggingAndReporting:
    def __init__(self, original_data, modified_data):
        self.original_data = original_data
        self.modified_data = modified_data

        # Set up logging
        logging.basicConfig(filename='preprocessing_log.txt', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    def log_preprocessing_step(self, step_name, parameters):
        logging.info(f"Preprocessing Step: {step_name}")
        logging.info(f"Parameters: {parameters}")

    def showReport(self):
        # Display the summary reports of the data before and after preprocessing
        print("\nOriginal Data Summary:")
        print(self.original_data.describe(include='all'))

        print("\nModified Data Summary:")
        print(self.modified_data.describe(include='all'))

    def generate_summary_report(self):
        # Generate summary reports of the data before and after preprocessing
        original_summary = self.original_data.describe(include='all')
        modified_summary = self.modified_data.describe(include='all')

        # Save the summary reports to CSV files
        original_summary.to_csv('original_data_summary.csv')
        modified_summary.to_csv('modified_data_summary.csv')

        logging.info("Summary Reports Generated and Saved")
