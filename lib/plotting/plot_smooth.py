import matplotlib.pyplot as plt
from initial_value_problem.get_time_values import get_time_values

def plot_smooth(df_smooth, df_raw):
    
    compositions = range (1,8)
    
    fig, _ = plt.subplots(3,3,figsize=(17,17))
    plt.suptitle("Smooth Data",fontsize=20)

    
    for comp in compositions:
        plt.subplot(3, 3, comp)
        
        raw = df_raw.loc[comp]
        raw.reset_index(drop=False, inplace=True)
        
        smooth = df_smooth.loc[comp]
        smooth.reset_index(drop=False, inplace=True)
        smooth.time += 1
        

        
        frame = '33'+str(comp)
        plt.subplot(frame)
        
        title = 'Composition ' + str(comp)
        plt.title(title,fontsize=15)
        plt.xlabel('Time (Days)', fontsize = 12)
        plt.ylabel('g/L or mM', fontsize = 12)
        l1 = plt.scatter(x=raw['time'], y=raw['acetate'], color='tab:orange')
        l2 = plt.scatter(x=raw['time'], y=raw['biomass'], color='tab:blue')
        l3 = plt.scatter(x=raw['time'], y=raw['butanol'], color='tab:purple')
        l4 = plt.scatter(x=raw['time'], y=raw['butyrate'], color='tab:red')
        l5 = plt.scatter(x=raw['time'], y=raw['ethanol'], color='tab:green')
        
        times = get_time_values(smooth)
        if len(times) != smooth.shape[0]: #2 trials

            cutoff = len(times)
            smooth1 = smooth.iloc[:cutoff, :]
            smooth2 = smooth.iloc[cutoff:, :] 
            
            plt.plot(smooth2['time'], smooth2['acetate'], color='tab:orange')
            plt.plot(smooth2['time'], smooth2['biomass'], color='tab:blue')
            plt.plot(smooth2['time'], smooth2['butanol'], color='tab:purple')
            plt.plot(smooth2['time'], smooth2['butyrate'], color='tab:red')
            plt.plot(smooth2['time'], smooth2['ethanol'], color='tab:green')
            
        else:

            smooth1 = smooth
        
        plt.plot(smooth1['time'], smooth1['acetate'], color='tab:orange')
        plt.plot(smooth1['time'], smooth1['biomass'], color='tab:blue')
        plt.plot(smooth1['time'], smooth1['butanol'], color='tab:purple')
        plt.plot(smooth1['time'], smooth1['butyrate'], color='tab:red')
        plt.plot(smooth1['time'], smooth1['ethanol'], color='tab:green')
        
    series_labels = ['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol']
    fig.legend(handles=[l1, l2, l3, l4, l5], labels = series_labels, loc='lower center', ncol=5)