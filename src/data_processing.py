from src.connecting_db import connect
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

def data_cleaning(final_df):
    '''Cleaning the data and performing feature engineering for better insight'''
    try:
        final_df['VendorName']=final_df['VendorName'].str.strip()
        final_df['Volume']=final_df['Volume'].astype('float64')
        final_df.fillna(0,inplace=True)
        final_df['VendorName'].unique()

        final_df['Gross_profit'] = final_df['Total_Sales_Dollars']-final_df['Total_Purchase_Dollars']
        final_df['ProfitMargin'] = (final_df['Gross_profit']/final_df['Total_Sales_Dollars'])*100
        final_df["StockTurnOver"] = final_df['Total_Sales_Quantity']/final_df['Total_purchase_Quantity']
        final_df['SalesToPurchaseRatio'] = final_df['Total_Sales_Dollars']/final_df['Total_Purchase_Dollars']

        float_cols = final_df.select_dtypes(include='float').columns
        for col in float_cols:
            final_df[col] = final_df[col].round(2) 


        final_df["ProfitMargin"] = pd.to_numeric(final_df["ProfitMargin"], errors="coerce")
        final_df["ProfitMargin"] = final_df["ProfitMargin"].replace([np.inf, -np.inf], 0)
        final_df["ProfitMargin"] = final_df["ProfitMargin"].fillna(0).round(2)

        return final_df
    except Exception as e:
        print(f"Unable to clean the data {e}")
