from initial_value_problem.get_time_values import get_time_values

import pandas as pd

def get_ml_conc_pred_df(ml_conc_pred_dict, smooth_data):
    compositions = range(1,8)
    output = pd.DataFrame()
    
    for comp in compositions:
        times = get_time_values(smooth_data.loc[comp])
        num_times = len(times)
        
        ml_conc_comp_pred_dict = ml_conc_pred_dict[f'composition_{comp}']
        predicted_concs = ml_conc_comp_pred_dict['test_predicted_concs']
        acetate = predicted_concs[:num_times*5:5]
        biomass = predicted_concs[1:num_times*5+1:5]
        butanol = predicted_concs[2:num_times*5+2:5]
        butyrate = predicted_concs[3:num_times*5+3:5]
        ethanol = predicted_concs[4:num_times*5+4:5]

        comp_output = pd.DataFrame({
            'composition': [comp]*num_times, 
            'time': times,
            'acetate': acetate,
            'biomass': biomass,
            'butanol': butanol,
            'butyrate': butyrate,
            'ethanol': ethanol})

        output = pd.concat([output , comp_output],sort=True)

    output.set_index(['composition', 'time'], inplace=True)
    return output