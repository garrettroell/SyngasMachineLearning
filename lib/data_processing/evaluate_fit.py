from scipy.stats import linregress
from sklearn import metrics

def evaluate_fit(df_fit, df_raw):

    compositions = range (1,8)
    fit_values = []
    raw_values = []
    r2_dict = {}
    rmse_dict = {}
    species_list = ['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol']

    for comp in compositions:

        raw = df_raw.loc[comp]
        raw.reset_index(drop=False, inplace=True)
        raw.time = raw.time.round(1)

        fit = df_fit.loc[comp]
        fit.reset_index(drop=False, inplace=True)
        fit.time += 1

        check_times = list(set(fit.time) & set(raw.time))

        fit = fit[fit['time'].isin(check_times)]
        raw = raw[raw['time'].isin(check_times)]

        comp_fit_values = []
        comp_raw_values = []  

        for row in raw.iterrows():
            raw_row = row[1]
            fit_row = fit[fit['time'] == raw_row.time]

            for species in species_list:
                comp_fit_values.append(fit_row[species].values[0])
                comp_raw_values.append(raw_row[species])

        _, _, r_value, _, _ = linregress(comp_fit_values, comp_raw_values)
        r2_dict[comp] = (r_value**2).round(3)
        
        comp_mse = metrics.mean_squared_error(comp_fit_values, comp_raw_values)
        rmse_dict[comp] = (comp_mse**0.5).round(3)

        fit_values.extend(comp_fit_values)
        raw_values.extend(comp_raw_values)

    _, _, r_value, _, _ = linregress(fit_values, raw_values)
    r2_overall = (r_value**2).round(3)
    
    mse_overall = metrics.mean_squared_error(fit_values, raw_values)
    rmse_overall = (mse_overall**0.5).round(3)
    
    return r2_overall , r2_dict, rmse_overall, rmse_dict