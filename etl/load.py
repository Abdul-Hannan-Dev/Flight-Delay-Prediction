from sqlalchemy import text
from datetime import date
import pandas as pd
def load_month(df, month, year, engine):
    if len(df)==0:
        raise ValueError('DataFrame should not be empty.')
    if month>12 or month<1:
        raise ValueError('Incorrect month.')
    start=date(year,month,1)
    if month<12:
        end=date(year,month+1,1)
    else:
        end=date(year+1,1,1)
    if (df['fl_date']<pd.Timestamp(start)).any() or (df['fl_date']>=pd.Timestamp(end)).any():
        raise ValueError(f"fl_date range {df['fl_date'].min()} to {df['fl_date'].max()} is outside {start} to {end}")
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM flights WHERE fl_date>=:start AND fl_date<:end"),{"start":start,"end":end})
        df.to_sql("flights", con=conn, if_exists='append', index=False,chunksize=25000)