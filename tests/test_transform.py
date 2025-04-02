import pandas as pd
import sys
import os

# Make sure Python can find your etl module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl.transform import transform_crypto_data

def test_transform_crypto_data():
    data = {
        'id': ['bitcoin', 'ethereum'],
        'symbol': ['btc', 'eth'],
        'current_price': [28000, 1800],
        'market_cap': [500000000, 200000000],
        'total_volume': [20000000, 15000000]
    }
    df = pd.DataFrame(data)
    transformed = transform_crypto_data(df)

    assert list(transformed.columns) == ['id', 'symbol', 'price_usd', 'market_cap', 'volume_24h']
    assert transformed['symbol'].iloc[0] == 'BTC'
    assert transformed.shape[0] == 2
