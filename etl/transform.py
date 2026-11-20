import pandas as pd
from datetime import datetime
NUMBER_COLS = [
    'month', 'day_of_week', 'crs_dep_time', 'crs_arr_time',
    'crs_elapsed_time', 'distance', 'arr_delay', 'is_delayed',
    'cancelled', 'diverted', 'dep_delay',
]
def transform(raw):
    df=raw[['MONTH','DAY_OF_WEEK','FL_DATE','OP_UNIQUE_CARRIER','ORIGIN','DEST','CRS_DEP_TIME','CRS_ARR_TIME','CRS_ELAPSED_TIME','DISTANCE','ARR_DELAY','CANCELLED','DIVERTED','DEP_DELAY']].copy()
    df.columns=df.columns.str.lower()
    df['fl_date']=df['fl_date'].str.split(' ',n=1).str[0]
    df['fl_date']=pd.to_datetime(df['fl_date'],format='%m/%d/%Y')
    df['is_delayed']=(df['arr_delay']>15).astype('Int16').mask(df['arr_delay'].isna())
    df[NUMBER_COLS] = df[NUMBER_COLS].astype("Int16")
    df=df[['fl_date', 'month', 'day_of_week', 'op_unique_carrier', 'origin', 'dest', 'crs_dep_time', 'crs_arr_time', 'crs_elapsed_time', 'distance', 'arr_delay', 'is_delayed', 'cancelled', 'diverted', 'dep_delay']]
    return df
raw=pd.read_csv(r"C:\Users\Team 1\Downloads\T_ONTIME_REPORTING.csv")
transform(raw)