import pandas as pd
import numpy as np
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor,  GradientBoostingRegressor

from ml_slope_model.get_X_y_arrays_for_slope import get_X_y_arrays_for_slope
from ml_general_functions.get_model_metrics import get_model_metrics

def get_ml_slope_prediction_dict(input_data, smooth_data, regressor):
    
    compositions = range(1,8)
    fit_data = {}
    
    for test_comp in compositions:
        
        train_comps = [ x for x in range(1,8) if x != test_comp]

        train_data = input_data.loc[train_comps,:]
        test_data = smooth_data.loc[test_comp,:]

        X_training, y_training = get_X_y_arrays_for_slope(train_data)
        X_testing, y_testing   = get_X_y_arrays_for_slope(test_data)

        if regressor == 'random forest':
            model = MultiOutputRegressor(RandomForestRegressor(n_estimators=200, max_depth=10, random_state=0))        
        elif regressor == 'gradient boosting':
            model = MultiOutputRegressor(GradientBoostingRegressor())
        else: 
            print('unknown regressor')
        model.fit(X_training, y_training)

        train_r2, train_mse, train_rmse, train_measured_slopes, train_predicted_slopes = get_model_metrics(model, X_training, y_training)
        test_r2, test_mse, test_rmse, test_measured_slopes, test_predicted_slopes = get_model_metrics(model, X_testing, y_testing)
        
        fit_data[f'composition_{test_comp}'] = {
                               "test_r2": test_r2,
                               "train_r2": train_r2,
                               "test_mse": test_mse,
                               "train_mse": train_mse,
                               "test_rmse": test_rmse,
                               "train_rmse": train_rmse,
                               "test_measured_slopes": test_measured_slopes,
                               "test_predicted_slopes": test_predicted_slopes,
                               "train_measured_slopes": train_measured_slopes,
                               "train_predicted_slopes": train_predicted_slopes,
                               "model": model,
                              }
    return fit_data