def transform_crypto_data(df):
    # Keep only the columns we care about
    df = df[['id', 'symbol', 'current_price', 'market_cap', 'total_volume']]

    # Rename columns to snake_case
    df.columns = ['id', 'symbol', 'price_usd', 'market_cap', 'volume_24h']

    # Clean up
    df = df.dropna()
    df['symbol'] = df['symbol'].str.upper()

    return df
