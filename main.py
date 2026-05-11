from etl.extract import extract
from etl.transform import transform
from etl.load import create_table, load
from database.query_data import query_last_7_days

# extract
raw_data = extract()
print(f"Extracted Data : {len(raw_data)}")

# transform
cleaned_data = transform(raw_data)
print(f"Transformed Data : {len(cleaned_data)}")

# load
create_table()
load(cleaned_data)

print("Data successfully loaded into SQLite")

# show database data
query_last_7_days()