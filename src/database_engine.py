import csv
import os
from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

output_ids = os.getenv('OUTPUT_FILE_UIDS')

# Database setup
engine = create_engine(os.getenv("DATABASE_URL"), echo = True)
if not database_exists(engine.url):
    engine = create_database(engine.url)

# print(database_exists(engine.url))
# metadata = MetaData(bind=engine)
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()

def parse_csv_and_insert_to_db(file_path: str):
    filename_with_extension = os.path.basename(file_path)
    filename_without_extension, extension = os.path.splitext(filename_with_extension)

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames  # Get the header of the CSV
        
        if headers is None:
            raise ValueError("CSV file has no headers.")
        
        table = Table(
            filename_without_extension, 
            metadata,
            *(Column(col, String if col in output_ids else String, primary_key=(col in output_ids)) for col in headers)
        )
        metadata.create_all(engine)

        # print(f"CSV Headers: {headers}")  # Log the headers
        
        # Insert rows into the database
        for row in reader:
            data = {key: row[key] for key in headers}
            insert_statement = table.insert().values(**data)
            session.execute(insert_statement)
        
        # Commit the transaction
        session.commit()
        print(f"Data successfully inserted into {filename_without_extension}: table.")
