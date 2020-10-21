def get_initial_values(df):
    
    df2 = df.copy()
    
    try:
        df2.reset_index(inplace=True,drop=False)
    except:
        pass
    
    try:
        df2.drop(columns=['trial'],inplace=True) 
    except:
        pass
    
    time_zeros = df2.loc[df2['time'] == 0]
    start = time_zeros.mean()
    initial_values =  [start['acetate'], start['biomass'], start['butanol'], start['butyrate'], start['ethanol']]
    
    return initial_values