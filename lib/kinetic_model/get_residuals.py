import pandas as pd
import numpy as np

from initial_value_problem.get_time_values import get_time_values
from initial_value_problem.get_initial_values import get_initial_values
from kinetic_model.solve_diff_eqs import solve_diff_eqs
from kinetic_model.get_kinetic_model_derivs import get_kinetic_model_derivs

def get_residuals(params, data_holder_list):

    df = data_holder_list

    times = get_time_values(df) 
    initial_values = get_initial_values(df)

    print('started solve diff eqs')
    sim_data = solve_diff_eqs(get_kinetic_model_derivs, initial_values, times, params)
    print('finished solve diff eqs')
    
    if len(times) != df.shape[0]: #2 trials
        cutoff = len(times)
        df1 = df.iloc[:cutoff, :]
        df2 = df.iloc[cutoff:, :]   

        diff1   = pd.DataFrame(index = times, columns = ['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol'])
        diff2   = pd.DataFrame(index = times, columns = ['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol'])
        
        diff1   = (sim_data-df1)
        diff2   = (sim_data-df2)

        residuals = np.concatenate([diff1.values.ravel(), diff2.values.ravel()])

    else:
        diff   = pd.DataFrame(index = times, columns = ['acetate','biomass', 'butanol', 'butyrate', 'ethanol'])
        diff   = (sim_data-df)

        resids = pd.DataFrame.to_numpy(diff,copy=True)
        residuals = np.concatenate(resids)
        
    return residuals