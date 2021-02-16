from machine_learning.get_X_y_arrays import get_X_y_arrays
import pandas as pd

def get_model_predictions(model_dict, input_df):
    model_predictions = {}
    ml_input, _ = get_X_y_arrays(input_df, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    for model_name in model_dict.keys():
        model = model_dict[model_name]
        prediction = model.predict(ml_input)
        prediction_df = pd.DataFrame(data=prediction, index=input_df.index, columns=['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol'])
        model_predictions[model_name] = prediction_df

    return model_predictions