import matplotlib.pyplot as plt

def plot_scatterplots(df,title):
    
    compositions = range (1,8)
    
    fig, _ = plt.subplots(3,3,figsize=(17,17))
    plt.suptitle(title,fontsize=20)

    
    for comp in compositions:
        plt.subplot(3, 3, comp)
        
        raw = df.loc[comp]
        raw.reset_index(drop=False, inplace=True)
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

    series_labels = ['acetate', 'biomass', 'butanol', 'butyrate', 'ethanol']
    fig.legend(handles=[l1, l2, l3, l4, l5], labels = series_labels, loc='lower center', ncol=5)