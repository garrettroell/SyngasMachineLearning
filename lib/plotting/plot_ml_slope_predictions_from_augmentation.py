from plot_ml_slope_predictions import plot_ml_slope_predictions

def plot_ml_slope_predictions_from_augmentation(fit_data_holder):
    
    for num_augment in fit_data_holder:
        fit_data = fit_data_holder[num_augment]
        plot_ml_slope_predictions(fit_data, f'ML Slope Predictions with {num_augment} augmentations')