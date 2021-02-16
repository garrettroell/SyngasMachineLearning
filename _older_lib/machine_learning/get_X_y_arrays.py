import numpy as np

def get_X_y_arrays_conc(input_data, specific_comps):


    input_data_copy = input_data.copy()
    input_data_copy = input_data_copy.loc[specific_comps]
    input_data_copy.reset_index(inplace=True)
    X  = input_data_copy [['time','acetate_0', 'biomass_0', 'butanol_0', 'butyrate_0', 'ethanol_0', 'CO', 'CO2', 'H2', 'flow rate']]
    y = input_data_copy  [['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol']]

    return np.array(X), np.array(y)

def get_X_y_arrays_slope(input_data, specific_comps):


    input_data_copy = input_data.copy()
    input_data_copy = input_data_copy.loc[specific_comps]
    input_data_copy.reset_index(inplace=True)
    X  = input_data_copy [['time','acetate', 'biomass', 'butanol', 'butyrate', 'ethanol', 'CO', 'CO2', 'H2', 'flow rate']]
    y = input_data_copy  [['acetate_Δ', 'biomass_Δ', 'butanol_Δ', 'butyrate_Δ', 'ethanol_Δ']]
 
    return np.array(X), np.array(y)