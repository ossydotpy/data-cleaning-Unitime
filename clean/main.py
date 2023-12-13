import argparse

from .cleaner import ExamScheduleProcessor


def main():
    parser = argparse.ArgumentParser(description="Process exam schedule data.")
    parser.add_argument("-f", help="Path to the data file.")
    parser.add_argument("--type", choices=["csv", "xlsx"], default="csv", help="File type (csv or xlsx).")
    args = parser.parse_args()

    processor = ExamScheduleProcessor(args.f, args.type)
    processor.read_data()
    processor.clean_data()
    processor.save_cleaned_data()


if __name__ == "__main__":
    main()
