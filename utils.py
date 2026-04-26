import pandas as pd

def preprocess(df):
    df = df.fillna(0)

    # Basic features
    df['TotalRooms'] = df['BedroomAbvGr'] + df['TotRmsAbvGrd']
    df['HouseAge'] = 2024 - df['YearBuilt']

    features = [
        'GrLivArea',
        'BedroomAbvGr',
        'FullBath',
        'TotalRooms',
        'HouseAge'
    ]

    return df[features]