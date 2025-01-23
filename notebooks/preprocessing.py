import numpy as np
import pandas as pd



def fill_null_values(df, null_fill, remove_rows=True):
    
    # Remove rows
    if ('remove_row' in null_fill.keys()) and (remove_rows):
        for row in null_fill['remove_row']:
            df = df.drop(row, axis=1)
    
    # Fill with zero
    if 'fill_w_zero' in null_fill.keys():
        for column in null_fill['fill_w_zero']:
            df[column] = df[column].fillna(0)
    
    # Fill with mean value
    if 'fill_w_mean' in null_fill.keys():
        for column in null_fill['fill_w_mean']:
            df[column] = df[column].fillna(null_fill['fill_w_mean_val'][column])

    # Fill with top value
    if 'fill_w_top' in null_fill.keys():
        for column, i in zip(null_fill['fill_w_top'], range(len(null_fill['fill_w_top']))):
            df[column] = df[column].fillna(null_fill['fill_w_top_val'][i])

    # Return data frame
    return df


if __name__ == '__main__':
    # FOR TESTING
    train_df = pd.read_csv('datasets/train.csv')
    test_df = pd.read_csv('datasets/test.csv')   

    fill_w_mean_val = train_df[['LotFrontage', 'Utilities', 'Exterior1st', 'Exterior2nd', 'BsmtFinSF1', 
               'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath',
               'KitchenQual', 'Functional', 'GarageCars', 'GarageArea', 'SaleType']].describe().mean()

    null_fill = {
    'remove_row': ['Electrical'],
    'fill_w_zero': ['Alley', 'MasVnrType', 'MasVnrArea', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 
               'BsmtFinType1', 'BsmtFinType2', 'FireplaceQu', 'GarageType', 'GarageYrBlt', 
               'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence'],
    'fill_w_mean': ['LotFrontage', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath', 'GarageCars', 'GarageArea'],
    'fill_w_mean_val': fill_w_mean_val,
    'fill_w_top': ['Utilities', 'Exterior1st', 'Exterior2nd', 'KitchenQual', 'Functional', 'SaleType'],
    'fill_w_top_val': ['AllPub', 'VinylSd', 'VinylSd', 'TA', 'Typ', 'WD'],
    }

    train_df = fill_null_values(train_df, null_fill=null_fill)
    test_df = fill_null_values(test_df, null_fill=null_fill, remove_rows=False)