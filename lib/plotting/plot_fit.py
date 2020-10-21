import matplotlib.pyplot as plt
from data_processing.evaluate_fit import evaluate_fit


def plot_fit(df_fit, df_raw, title):
    
    _ , _, rmse_overall, rmse_dict = evaluate_fit(df_fit, df_raw)
    title += f' Overall rmse = {rmse_overall}'
    
    fig, _ = plt.subplots(3,3,figsize=(17,17))
    plt.suptitle(title ,fontsize=20)

    
    for comp in range(1, 8):
        plt.subplot(3, 3, comp)
        
        raw = df_raw.loc[comp]
        raw.reset_index(drop=False, inplace=True)
        
        fit = df_fit.loc[comp]
        fit.reset_index(drop=False, inplace=True)
        fit.time += 1
        
        frame = '33'+str(comp)
        plt.subplot(frame)
        
        title = f'Comp {comp} rmse = {rmse_dict[comp]}' 
        plt.title(title,fontsize=15)
        plt.xlabel('Time (Days)', fontsize = 12)
        plt.ylabel('g/L or mM', fontsize = 12)
        l1 = plt.scatter(x=raw['time'], y=raw['acetate'], color='tab:orange')
        l2 = plt.scatter(x=raw['time'], y=raw['biomass'], color='tab:blue')
        l3 = plt.scatter(x=raw['time'], y=raw['butanol'], color='tab:purple')
        l4 = plt.scatter(x=raw['time'], y=raw['butyrate'], color='tab:red')
        l5 = plt.scatter(x=raw['time'], y=raw['ethanol'], color='tab:green')
        
        plt.plot(fit['time'], fit['acetate'], color='tab:orange')
        plt.plot(fit['time'], fit['biomass'], color='tab:blue')
        plt.plot(fit['time'], fit['butanol'], color='tab:purple')
        plt.plot(fit['time'], fit['butyrate'], color='tab:red')
        plt.plot(fit['time'], fit['ethanol'], color='tab:green')
        
    series_labels = ['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol']
    fig.legend(handles=[l1, l2, l3, l4, l5], labels = series_labels, loc='lower center', ncol=5)
    