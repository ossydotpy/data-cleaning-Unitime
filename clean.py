import argparse
import pandas as pd
from datetime import datetime, timedelta


parser = argparse.ArgumentParser(description="Process exam schedule data.")
parser.add_argument("data_file", help="Path to the data file.")

args = parser.parse_args()

try:
    df = pd.read_csv(args.data_file)
except FileNotFoundError:
    print(f"Error: File '{args.data_file}' not found.")
    exit()
except (pd.errors.ParserError, UnicodeDecodeError):
    try:
        df = pd.read_excel(args.data_file)
    except FileNotFoundError:
        print(f"Error: File '{args.data_file}' not found.")
        exit()
    except Exception as e:
        print(f"Error: Unable to read file '{args.data_file}': {e}")
        exit()
try:
    df = df.rename(columns={'Examination': 'exam_name', 'Date': 'Date', 'Day':'Day',
                            'Room': 'Room', 'Capacity': 'Capacity', ' Instructor': 'Instructor',
                             ' Student\nConflicts': 'Student_Conflict', 
                             ' Instructor\nConflicts': 'Instructor_Conflict'})
except KeyError as e:
    print(f"Error: Column '{e.args[0]}' not found in the data file.")
    exit()


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


df['Date'] = df['Date'].apply(lambda x: datetime.strftime(x, '%d-%b-%Y'))
df[["Start", "End"]] = df["Time"].str.split(' - ', expand=True)
df['Start'] = df['Start'].apply(format_time)
df['End'] = df['End'].apply(format_time)
df = df.sort_values(by=['Date', 'Start'])
df['is_faculty_wide'] = 0

df.drop(columns=['Enrollment','Seating\nType', 'Time'], inplace=True)

cols = ['exam_name', 'Date', 'Day', 'Start', 'End', 'Room', 'Capacity', 'Instructor',
        'Student_Conflict', 'Instructor_Conflict', 'is_faculty_wide']
df = df.reindex(columns=cols)


cleaned_data_file = f"cleaned-{args.data_file}"
df.to_csv(cleaned_data_file, index=False)

print(f"Cleaned data saved to: {cleaned_data_file}")
