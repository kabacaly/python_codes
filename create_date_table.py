def create_date_table(start_date='2011-11-01', end_date='2018-04-30'):
    df = pd.DataFrame({'Date': pd.date_range(start_date, end_date)})
    return df
