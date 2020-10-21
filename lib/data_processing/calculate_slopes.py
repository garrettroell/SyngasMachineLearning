import pandas as pd
from initial_value_problem.get_gas_comp import get_gas_comp

def calculate_slopes(df_orig):  

    df = df_orig.copy()
    if df.index.names[1] != 'trial':
        df.reset_index(inplace=True)
        df.insert(0, 'trial', 0)
        df.set_index(['composition', 'trial', 'time'], inplace=True)
        
    gas_comp = get_gas_comp() 
    gas_data = pd.DataFrame.from_dict(gas_comp,orient = 'index',columns = ['CO','CO2','H2','Flow Rate'])

    slope_cols = ['Δ acetate', 'Δ biomass', 'Δ butanol', 'Δ butyrate', 'Δ ethanol']
    change_data = {}
    
    df.sort_index(inplace=True)
    
    for row_num, current_index in enumerate(df.index):

        # Exception occurs at the very bottom of the dataframe
        try:
            next_index = df.index[row_num+1]
        except IndexError:
            next_index = current_index
        
        current_time = current_index[2]
        next_time = next_index[2]
        time_delta = next_time - current_time
        
        #This is true unless comparing the last time of one experiment to the first time of the next
        if time_delta > 0:

            current_values = df.loc[current_index].values
            next_values = df.loc[next_index].values
            rates = list((next_values - current_values)/time_delta)
            change_data[current_index] = rates
            
    change_data_df = pd.DataFrame.from_dict(change_data, 
        orient='index',
        columns = slope_cols)
    
    change_data_df.index = pd.MultiIndex.from_tuples(change_data.keys(), names=('composition', 'trial','time'))
    
    slope_info = df.merge(change_data_df, left_index = True, right_index = True)

    #Add gas composition to data
    slope_info.reset_index(inplace=True)
    slope_info.set_index('composition', inplace=True)
    slope_info = slope_info.merge(gas_data, left_index = True, right_index = True)

    return slope_info