import pandas as pd


def transform_data(features_df, sales_df, stores_df):
    
    #change date from object to datetime
    features_df['Date'] = pd.to_datetime(features_df['Date'])
    sales_df['Date'] = pd.to_datetime(sales_df['Date'], dayfirst= True)


    markdown_colms = ['MarkDown1', 'MarkDown2', 'MarkDown3' 'MarkDown4', 'MarkDown5']
    features_df = features_df.drop(columns = markdown_colms, errors = 'ignore')

    dim_store = stores_df.drop_duplicates().reset_index(drop = True)

    dim_date = sales_df[['Date', 'IsHoliday']].drop_duplicates().copy()

    dim_date['year'] = dim_date['Date'].dt.year
    dim_date['month'] = dim_date['Date'].dt.month
    dim_date['week'] = dim_date['Date'].dt.isocalendar().week.astype(int)

    dim_feature = features_df.drop_duplicates().reset_index(drop = True)

    fact_sales = sales_df.copy()

    dim_date = normalize(dim_date)
    dim_feature = normalize(dim_feature)
    dim_store = normalize(dim_store)
    fact_sales = normalize(fact_sales)

    return fact_sales, dim_store, dim_date, dim_feature


def normalize(df):
    df.columns = df.columns.str.lower().str.replace('', '_') 
    return df

