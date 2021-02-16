def add_slope_values(df):

  acetate_Δ = []
  biomass_Δ = []
  butanol_Δ = []
  butyrate_Δ = []
  ethanol_Δ = []

  old_comp = 0
  old_tri = 0

  for index, _ in df.iterrows():
    new_comp = index[0]
    new_tri = index[1]

    if (new_comp == old_comp and new_tri == old_tri):
      Δ_time = index[2] - old_index[2]

      acetate_Δ.append((df.loc[index]['acetate']-df.loc[old_index]['acetate'])/Δ_time)
      biomass_Δ.append((df.loc[index]['biomass']-df.loc[old_index]['biomass'])/Δ_time)
      butanol_Δ.append((df.loc[index]['butanol']-df.loc[old_index]['butanol'])/Δ_time)
      butyrate_Δ.append((df.loc[index]['butyrate']-df.loc[old_index]['butyrate'])/Δ_time)
      ethanol_Δ.append((df.loc[index]['ethanol']-df.loc[old_index]['ethanol'])/Δ_time)
    else: 
      acetate_Δ.append(0)
      biomass_Δ.append(0)
      butanol_Δ.append(0)
      butyrate_Δ.append(0)
      ethanol_Δ.append(0)

    old_comp = index[0]
    old_tri = index[1]
    old_index = index

  df['acetate_Δ'] = acetate_Δ
  df['biomass_Δ'] = biomass_Δ
  df['butanol_Δ'] = butanol_Δ
  df['butyrate_Δ'] = butyrate_Δ
  df['ethanol_Δ'] = ethanol_Δ

  return df