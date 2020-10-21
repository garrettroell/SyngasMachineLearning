import pandas as pd
from initial_value_problem.get_initial_values import get_initial_values
from initial_value_problem.get_time_values import get_time_values
from kinetic_model.solve_diff_eqs import solve_diff_eqs
from kinetic_model.get_kinetic_model_derivs import get_kinetic_model_derivs


def get_kinetic_model_data(df, result_dict):
    
    df2 = df.copy()
    fit_data = pd.DataFrame(columns = ['acetate','biomass', 'butanol', 'butyrate', 'ethanol'])
    
    for i in range(1,8):
        comp = df2.loc[i]
        comp.reset_index(drop=False, inplace=True)
        comp.drop(columns=['trial'],inplace=True) 
        comp.set_index('time',drop=True, inplace=True)
        initial_values = get_initial_values(comp)
        times = get_time_values(comp)

        params = result_dict[i].params

        sim_data = solve_diff_eqs(get_kinetic_model_derivs, initial_values, times, params)
        sim_data.index.rename('time', inplace=True)
        sim_data.reset_index(inplace=True, drop=False)
        sim_data.insert(0, "composition", i)
        
        fit_data =  pd.concat([fit_data , sim_data],sort=True)
    
    fit_data.set_index(['composition','time'],drop=True,inplace=True)    
    return fit_data