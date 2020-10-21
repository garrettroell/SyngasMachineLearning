import pandas as pd
from scipy.integrate import solve_ivp 
from ml_slope_model.get_ml_model_derivs import get_ml_model_derivs

def solve_diff_eqs_ml(initial_values, times, gas_comp, ml_model):
   
    t_range = [times[0],times[-1]]
    sol = solve_ivp(lambda t, y: get_ml_model_derivs(t, y, gas_comp, ml_model), t_range, initial_values,t_eval=times, rtol = 0.01, atol = 0.01)

    sim_data = pd.DataFrame(index = times, columns = ['acetate','biomass', 'butanol', 'butyrate', 'ethanol'])

    sim_data['acetate']  = sol.y[0]
    sim_data['biomass']  = sol.y[1]
    sim_data['butanol']  = sol.y[2]
    sim_data['butyrate'] = sol.y[3]
    sim_data['ethanol']  = sol.y[4]
    sim_data.clip(lower=0, inplace=True)

    return sim_data