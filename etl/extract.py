import pandas as pd


def extract_data():

    #get csv files
    features_df = pd.read_csv(r'data/Features_dataset.csv')
    sales_df = pd.read_csv(r'data/sales_dataset.csv')
    stores_df = pd.read_csv(r'data/stores_dataset.csv')


    #check columns
    print('Features Dataset')
    print(features_df.head())
    print(features_df.dtypes)
    print("---------------------------")


    print("Sales Dataset")
    print(sales_df.head())
    print(sales_df.dtypes)
    print("---------------------------")
    
    print('Stores Dataset')
    print(stores_df.head())
    print(stores_df.dtypes)
    print("---------------------------")

    return features_df, sales_df, stores_df

extract_data()


