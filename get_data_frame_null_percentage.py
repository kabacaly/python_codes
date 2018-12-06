def null_df(df, sort=True):
    nulls = df.isnull().sum()
    df_nulls = pd.DataFrame({'col':nulls.index.values, 'val':nulls.values})
    df_nulls['perc'] = df_nulls['val'] / df.shape[0] * 100
    if sort:
        df_nulls.sort_values('perc', ascending=False, inplace=True)
    return df_nulls
