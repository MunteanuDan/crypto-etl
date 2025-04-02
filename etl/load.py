import sqlalchemy

def load_data_to_postgres(df, db_uri, table_name='crypto_prices'):
    engine = sqlalchemy.create_engine(db_uri)
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(df)} rows into '{table_name}'")
