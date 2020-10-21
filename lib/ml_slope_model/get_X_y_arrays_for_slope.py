import numpy as np

def get_X_y_arrays_for_slope(input_data):

    input_data_copy = input_data.copy()
    input_data_copy.reset_index(inplace=True)
    X  = input_data_copy [['CO', 'CO2', 'H2', 'Flow Rate', 'acetate', 'biomass', 'butanol', 'butyrate', 'ethanol']]
    y = input_data_copy  [['Δ acetate', 'Δ biomass', 'Δ butanol', 'Δ butyrate', 'Δ ethanol' ]]

    return np.array(X), np.array(y)