import pandas as pd
from kinetic_model.fit_parameters import fit_parameters
from kinetic_model.valid_params import valid_params

def get_kinetic_parameter_dictionary(df, num_restarts): 
    """takes in smoothed data and returns a dictionary of 
        the best parameters for each composition"""
    
    df2 = df.copy()
    
    fit_data = pd.DataFrame()
    result_dict = {}
    ci_dict = {}
    compositions = range(1,8) 
    for composition in compositions:
        print('composition:', composition)
        
        best_ssr = 100_000_000
        best_result = 0

        comp = df2.loc[composition]
        comp.reset_index(drop=False, inplace=True)
        comp.drop(columns=['trial'],inplace=True)
        comp.set_index('time',drop=True, inplace=True)

        for j in range(num_restarts):
            result = fit_parameters(comp)
            print(valid_params(result.params))
            ssr =result.chisqr
            print(f'Composition {composition}: Search {j+1} of {num_restarts}, ssr: {ssr}, valid: {valid_params(result.params)}')
            if ssr < best_ssr and valid_params(result.params):
                best_ssr = ssr
                best_result = result

        result_dict[composition] = best_result
        
        #ci_dict[composition] = get_confidence_interval(comp, result)
        

    return result_dict