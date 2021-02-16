def subtract_one_day(df):
    df_copy = df.copy()
    df_copy.reset_index(inplace=True)
    df_copy = df_copy[df_copy['time'] > 1]
    df_copy['time'] = df_copy['time'] - 1
    df_copy.set_index(['composition', 'trial', 'time'], inplace=True, drop = True)
    return df_copy