from os import getenv
from database_engine import parse_csv_and_insert_to_db
from utils import list_files_by_type

# Grab CSV Output Data files
output_dir = getenv('OUTPUT_FILE_DIRECTORY')
csv_files = list_files_by_type(directory=output_dir)

# Process and add files to SQL Database
for csv_file in csv_files:
    csv_file_path = f'{output_dir}/{csv_file}'
    try:
        parse_csv_and_insert_to_db(file_path=csv_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")
print("Data successfully inserted into database...")
