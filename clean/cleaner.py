import pandas as pd
from datetime import datetime, timedelta


class ExamScheduleProcessor:
    """
    Class to process exam schedule data from CSV or XLSX files.
    """
    def __init__(self, data_file, file_type):
        self.data_file = data_file
        self.file_type = file_type
        self.df = None

    @staticmethod
    def format_time(time_str):
        """
        Function to format time from '3:30a' or '3:30p'.
        """
        time_str = time_str.strip()
        try:
            if time_str.endswith('a'):
                dt = datetime.strptime(time_str[:-1], '%I:%M')
            elif time_str.endswith('p'):
                dt = datetime.strptime(time_str[:-1], '%I:%M') + timedelta(hours=12)
            else:
                raise ValueError
        except ValueError:
            print(f"Error: Invalid time format for '{time_str}'. Skipping...")
            return None
        return dt.strftime('%I:%M %p')

    def read_data(self):
        """Reads data from CSV or XLSX file based on the specified type."""
        if self.file_type == "csv":
            try:
                self.df = pd.read_csv(self.data_file)
            except FileNotFoundError:
                print(f"Error: File '{self.data_file}' not found.")
                exit()
        elif self.file_type == "xlsx":
            try:
                self.df = pd.read_excel(self.data_file)
            except FileNotFoundError:
                print(f"Error: File '{self.data_file}' not found.")
                exit()
        else:
            print(f"Error: Invalid file type '{self.file_type}'. Please specify 'csv' or 'xlsx'.")
            exit()

    def clean_data(self):
        """Cleans and prepares the data for further processing."""
        try:
            self.df = self.df.rename(columns={
                'Examination': 'exam_name',
                'Date': 'Date',
                'Day': 'Day',
                'Room': 'Room',
                'Capacity': 'Capacity',
                'Instructor': 'Instructor',
                'Student\nConflicts': 'Student_Conflict',
                'Instructor\nConflicts': 'Instructor_Conflict'})
        except KeyError as e:
            print(f"Error: Column '{e.args[0]}' not found in the data file.")
            exit()

        # Clean and format date and time
        if self.file_type == 'csv':
            self.df['Date'] = self.df['Date'].apply(lambda x: datetime.strptime(x, '%d-%b-%y'))
        elif self.file_type == 'xlsx':
            self.df['Date'] = self.df['Date'].apply(lambda x: datetime.strftime(x, '%d-%b-%Y'))

        self.df[["Start", "End"]] = self.df["Time"].str.split(' - ', expand=True)
        self.df['Start'] = self.df['Start'].apply(self.format_time)
        self.df['End'] = self.df['End'].apply(self.format_time)

        # Sort data and set default values
        self.df = self.df.sort_values(by=['Date', 'Start'])
        self.df['is_faculty_wide'] = 0

        # Drop unnecessary columns
        self.df.drop(columns=['Enrollment', 'Seating\nType', 'Time'], inplace=True)

        # Reorder columns
        self.df = self.df.reindex(columns=[
            'exam_name', 'Date', 'Day', 'Start', 'End', 'Room', 'Capacity', 'Instructor',
            'Student_Conflict', 'Instructor_Conflict', 'is_faculty_wide'])

    def save_cleaned_data(self):
        """Saves the cleaned data to a new CSV file."""
        cleaned_data_file = f"cleaned-{self.data_file}"
        self.df.to_csv(cleaned_data_file, index=False)
        print(f"Cleaned data saved to: {cleaned_data_file}")

