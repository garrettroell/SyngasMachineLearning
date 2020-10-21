import pandas as pd
import numpy as np
from scipy.signal import savgol_filter 

def smooth_interpolate_truncate(df,delta):
    """delta = step size"""
    savgol0 = lambda x: savgol_filter(x, 15, 2, deriv=0)
    smoothed_data = pd.DataFrame()
    
    composition = range (1,8)
    trial = [1,2]
    
    for comp in composition:
        for tri in trial:
            if (comp == 5 and tri == 2) or (comp == 6 and tri == 2) or (comp == 7 and tri == 2):
                pass
            else:
                section = df.loc[comp,tri]

                times = section.index
                max_time = times[-1] + delta
                new_times = np.arange(0,max_time, delta)  
                section = section.reindex(section.index.union(new_times))
                section = section.interpolate()
                section = section.round(3)
                times_to_remove = set(times) - (set(times) & set(new_times))
                section = section.loc[~section.index.isin(times_to_remove)]
            
                smooth=section.apply(savgol0)

                smooth.insert(0, "time", smooth.index)
                smooth.insert(0, "trial", tri)
                smooth.insert(0, "composition", comp)
                smoothed_data = pd.concat([smoothed_data , smooth],sort=True)


    smoothed_data.set_index(['composition','trial','time'],drop=True,inplace=True)
    smoothed_data.clip(lower=0,inplace=True)
        
    times_to_drop = np.arange(0,1,delta)
    smoothed_data = smoothed_data.drop(index =times_to_drop, level ='time')

    # work around to change index values
    smoothed_data.reset_index(drop=False,inplace=True)
    smoothed_data['time'] = round (smoothed_data['time']-1,1)
    smoothed_data.set_index(['composition','trial','time'],drop=True,inplace=True)
    
    return smoothed_data