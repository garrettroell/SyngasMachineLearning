def get_time_values(df):
    
    df2 = df.copy()
    
    try:
        df2.reset_index(inplace=True,drop=False)
    except:
        pass

    t_values = df2.time
    t_values.drop_duplicates(inplace=True)
    times = list(t_values)
    
    return times