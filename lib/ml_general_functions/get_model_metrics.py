from scipy.stats import linregress
from sklearn import metrics

def get_model_metrics(model, X_data, y_data):
    y_predicted = model.predict(X_data)
    y_measured_ravel = y_data.ravel().astype(float)
    y_predicted_ravel = y_predicted.ravel().astype(float)

    # slope, intercept, r_value, p_value, std_err
    _, _, r_value, _, _ = linregress(y_measured_ravel, y_predicted_ravel)
    r2 = (r_value**2).round(3)
    mse = metrics.mean_squared_error(y_measured_ravel, y_predicted_ravel)
    rmse = (mse**0.5).round(3)

    return r2, mse, rmse, y_measured_ravel, y_predicted_ravel