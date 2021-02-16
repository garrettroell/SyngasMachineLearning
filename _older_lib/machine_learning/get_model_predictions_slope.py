import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

def get_model_predictions_slope(model_dict, smooth_df, times_df):
    model_predictions = {}

    for model_name in model_dict.keys():
        print(model_name)
        model = model_dict[model_name]
        model_predictions[model_name] = get_prediction_df_for_single_model(smooth_df, times_df, model)

    return model_predictions

def get_prediction_df_for_single_model(smooth_df, times_df, model):
    # first starting values are found for each trial
    starting_value_df = get_only_starting_values(smooth_df)

    # dataframe for all trial predictions is initialized
    prediction_df = pd.DataFrame(columns = ['acetate','biomass', 'butanol', 'butyrate', 'ethanol'])

    # loops over each trial
    for index, series in starting_value_df.iterrows():
        composition, trial = index[0], index[1]

        # gets inputs for solve_diff_eqs function
        initial_values = [series['acetate'], series['biomass'], series['butanol'], series['butyrate'], series['ethanol']]
        gas_comp = [series['CO'], series['CO2'], series['H2'], series['flow rate']]
        time_range = get_time_range(smooth_df, composition, trial)
        time_list = get_times(times_df, composition, trial)

        # gets prediction dataframe for that trial
        output = solve_diff_eqs_ml(initial_values, time_range, time_list, gas_comp, model)

        # adds trial dataframe to all trial dataframe
        output.index.rename('time', inplace=True)
        output.reset_index(inplace=True, drop=False)
        output.insert(0, "composition", composition)
        output.insert(0, "trial", trial)    
        prediction_df =  pd.concat([prediction_df , output], sort=True)
    
    prediction_df.set_index(['composition', 'trial', 'time'], drop=True, inplace=True)    
    return prediction_df


def get_only_starting_values (smooth_df):
    df = smooth_df.reset_index(inplace=False, drop=False)
    df = df[df['time'] == 0]
    df.set_index(['composition', 'trial', 'time'], drop=True, inplace=True)
    return df


def get_time_range(smooth_df, composition, trial):
    df = smooth_df.reset_index(inplace=False, drop=False)
    df = df[df['composition'] == composition]
    df = df[df['trial'] == trial]

    time_range = [0, max(df['time'])]
    return time_range

def get_times(smooth_df, composition, trial):
    df = smooth_df.reset_index(inplace=False, drop=False)
    df = df[df['composition'] == composition]
    df = df[df['trial'] == trial]

    time_list = list(df['time'])
    return time_list

def solve_diff_eqs_ml(initial_values, t_range, times_list, gas_comp, ml_model):
   
    # t_range = [times[0],times[-1]]
    sol = solve_ivp(lambda t, y: get_ml_model_derivs(t, y, gas_comp, ml_model), t_range, initial_values, t_eval=times_list, rtol = 0.01, atol = 0.01)

    sim_data = pd.DataFrame(index = times_list, columns = ['acetate','biomass', 'butanol', 'butyrate', 'ethanol'])

    sim_data['acetate']  = sol.y[0]
    sim_data['biomass']  = sol.y[1]
    sim_data['butanol']  = sol.y[2]
    sim_data['butyrate'] = sol.y[3]
    sim_data['ethanol']  = sol.y[4]
    sim_data.clip(lower=0, inplace=True)

    return sim_data 

def get_ml_model_derivs(t, y, gas_comp, ml_model):

    dy = []
    # makes sure all values are non-negative
    for counter,conc in enumerate(y,0):
        if conc < 0:
            y[counter] = 0
    
    # the asterisks unpacks the contents of iterables
    ml_input_list = [[*[t], *y, *gas_comp]]
    ml_input_array = np.array(ml_input_list)
    # print(ml_model.predict(ml_input_array))

    for slope in ml_model.predict(ml_input_array)[0]:
        if slope > 100:
            slope = 100
        if slope < -100:
            slope = -100
        dy.append(slope)
        
    return dy 