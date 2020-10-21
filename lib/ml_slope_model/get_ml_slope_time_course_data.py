import pandas as pd
from initial_value_problem.get_initial_values import get_initial_values
from initial_value_problem.get_time_values import get_time_values
from initial_value_problem.get_gas_comp import get_gas_comp
from ml_slope_model.solve_diff_eqs_ml import solve_diff_eqs_ml

#smooth data is needed for data point/initial values
def get_ml_slope_time_course_data(slope_ml_dict, smooth_data):
  compositions = range(1,8)
  sim_df = pd.DataFrame()

  print()
  for comp in compositions:
    print(f'comp {comp}')
    comp_df = smooth_data.loc[comp]
    initial_values = get_initial_values(comp_df)
    times = get_time_values(comp_df)
    gas_comp = get_gas_comp()[comp]
    ml_model=slope_ml_dict[f'composition_{comp}']['model']

    sim_comp_df = solve_diff_eqs_ml(initial_values, times, gas_comp, ml_model)

    sim_comp_df.index.rename('time', inplace=True)
    sim_comp_df.reset_index(inplace=True, drop=False)
    sim_comp_df.insert(0, "composition", comp)

    sim_df =  pd.concat([sim_df , sim_comp_df],sort=True)

  sim_df.set_index(['composition','time'], drop=True, inplace=True) 

  return(sim_df)