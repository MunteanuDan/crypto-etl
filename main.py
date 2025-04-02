from etl.extract import extract_crypto_data
from etl.transform import transform_crypto_data
from etl.load import load_data_to_postgres

DB_URI = 'postgresql+psycopg2://postgres:stud@localhost:5432/cryptodb'

df = extract_crypto_data()
df = transform_crypto_data(df)
print(df)

load_data_to_postgres(df, DB_URI)
