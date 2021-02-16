def add_initial_values(df, smooth_df):

    acetate_0 = []
    biomass_0 = []
    butanol_0 = []
    butyrate_0 = []
    ethanol_0 = []

    for index, row in df.iterrows():
      comp = index[0]
      tri = index[1]
      
      acetate_0.append(smooth_df.loc[(comp,tri,0)]['acetate'])
      biomass_0.append(smooth_df.loc[(comp,tri,0)]['biomass'])
      butanol_0.append(smooth_df.loc[(comp,tri,0)]['butanol'])
      butyrate_0.append(smooth_df.loc[(comp,tri,0)]['butyrate'])
      ethanol_0.append(smooth_df.loc[(comp,tri,0)]['ethanol'])


    df['acetate_0'] = acetate_0
    df['biomass_0'] = biomass_0
    df['butanol_0'] = butanol_0
    df['butyrate_0'] = butyrate_0
    df['ethanol_0'] = ethanol_0

    return df