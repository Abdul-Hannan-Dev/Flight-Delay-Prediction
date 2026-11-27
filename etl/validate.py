import pandas as pd
def validate(df):
    empty_check=df[['fl_date', 'month', 'day_of_week', 'op_unique_carrier', 'origin', 'dest', 'crs_dep_time', 'crs_arr_time', 'distance', 'cancelled', 'diverted']]
    if empty_check.isna().sum().any() != False:
        columns_with_na_values=[]
        for i,j in zip(empty_check.columns,empty_check.isna().any() != False):
            if j==True:
                columns_with_na_values.append(i)
        raise ValueError(f'column(s): "{", ".join(columns_with_na_values)}" have empty values')
    if (df['fl_date'].dt.month!=df['month']).any():
        raise ValueError(f"The month in 'fl_date' and 'month' do not match")
    if (df['day_of_week'].min()>=1 and df['day_of_week'].max()<=7)!=True:
        raise ValueError(f"The values in column 'day_of_week' are not between 1 and 7")
    if (df['crs_dep_time'].min()>=0 and df['crs_dep_time'].max()<=2359)!=True:
        raise ValueError(f"The values in column 'crs_dep_time' are not between 0 and 2359")
    if (df['distance'].min()>0)!=True:
        raise ValueError(f"The values in column 'distance' are not positive")
    if (df['crs_elapsed_time']<=0).any()==True:
        raise ValueError(f"The values in column 'crs_elapsed_time' are not positive")
    if not df['is_delayed'].isna().equals(df['arr_delay'].isna()):
        raise ValueError(f"'is_delayed' and 'arr_delay' columns have mismatched NaN values")