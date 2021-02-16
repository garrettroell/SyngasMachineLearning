from scipy.stats import linregress
from sklearn import metrics

def get_pearson_r2 (measured, predicted):
    # slope, intercept, r_value, p_value, std_err
    _, _, r_value, _, _ = linregress(measured, predicted)
    r2 = (r_value**2)
    return r2

def get_rmse (measured, predicted):
    mse = metrics.mean_squared_error(measured, predicted)
    rmse = (mse**0.5)
    return rmse