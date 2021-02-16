import pandas as pd
from machine_learning.get_model_metrics import get_pearson_r2, get_rmse

#These functions need to be in notebooks so that display function can run


def evaluate_models_6(pred_df_dict, raw_df, metric):
    species_set = ['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol']
    test_comp_set=[1,2,3,4,5,6]
    index_set = ['gradient boosting, raw', 'random forest, raw', 'support vector, raw', 'neural net, raw', 'lasso, raw', 'gradient boosting, smooth', 'random forest, smooth', 'support vector, smooth', 'neural net, smooth', 'lasso, smooth']
    
    for species in species_set:
        data = {}
        for test_comp in test_comp_set:
            data[test_comp] = []
            for model_name in pred_df_dict.keys():
                if str(test_comp) in model_name:
                    predicted_species_values = list(pred_df_dict[model_name].loc[test_comp][species])
                    measured_species_values = list(raw_df.loc[test_comp][species])

                    r2 = get_pearson_r2(measured_species_values, predicted_species_values)
                    rmse = get_rmse (measured_species_values, predicted_species_values)
                    if metric == 'r2':
                        data[test_comp].append(r2)
                    elif metric == 'rmse':
                        data[test_comp].append(rmse)
                    else:
                        print('unknown metric')
        species_data = pd.DataFrame.from_dict(data)
        species_data[f'model for {species}'] = index_set
        species_data.set_index(f'model for {species}', inplace=True, drop=True)
        # display(species_data)

def evaluate_models_7(pred_df_dict, raw_df, metric):
    species_set = ['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol']
    test_comp_set=[1,2,3,4,5,6,7]
    index_set = ['gradient boosting, raw', 'random forest, raw', 'support vector, raw', 'neural net, raw', 'lasso, raw', 'gradient boosting, smooth', 'random forest, smooth', 'support vector, smooth', 'neural net, smooth', 'lasso, smooth']
    
    for species in species_set:
        data = {}
        for test_comp in test_comp_set:
            data[test_comp] = []
            for model_name in pred_df_dict.keys():
                # print(model_name)
                if str(test_comp) in model_name:
                    predicted_species_values = list(pred_df_dict[model_name].loc[test_comp][species])
                    measured_species_values = list(raw_df.loc[test_comp][species])

                    r2 = get_pearson_r2(measured_species_values, predicted_species_values)
                    rmse = get_rmse (measured_species_values, predicted_species_values)
                    if metric == 'r2':
                        data[test_comp].append(r2)
                    elif metric == 'rmse':
                        data[test_comp].append(rmse)
                    else:
                        print('unknown metric')
        species_data = pd.DataFrame.from_dict(data)
        species_data[f'model for {species}'] = index_set
        species_data.set_index(f'model for {species}', inplace=True, drop=True)
        # display(species_data)