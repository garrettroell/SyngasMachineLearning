import pandas as pd
from scipy.integrate import solve_ivp 

def solve_diff_eqs(derivative_function, initial_values, t_values, params):
    
    t_range = [t_values[0],t_values[-1]]
    sol = solve_ivp(lambda t, y: derivative_function(t, y, params), t_range, initial_values,t_eval=t_values, method ='BDF')

    sim_data = pd.DataFrame(index = t_values, columns = ['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol'])

    try:
        sim_data['acetate']  = sol.y[0]
        sim_data['biomass']  = sol.y[1]
        sim_data['butanol']  = sol.y[2]
        sim_data['butyrate'] = sol.y[3]
        sim_data['ethanol']  = sol.y[4]
    except:
        print('overflow in diff eq solver')
        sim_data['acetate']  = 0
        sim_data['biomass']  = 0
        sim_data['butanol']  = 0
        sim_data['butyrate'] = 0
        sim_data['ethanol']  = 0

    return sim_data