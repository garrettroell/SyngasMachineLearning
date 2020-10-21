from lmfit import Parameters
from kinetic_model.valid_params import valid_params
import random

def get_rand_params():
    params_valid = False
    
    while (params_valid == False):
        remain = 1
        params = Parameters()
        params.add('t_switch', value=round(random.uniform(0.75,3),3), min=0, max=3)

        params.add('V_in_1', value=round(random.uniform(0,150),3), min=0, max=150)
        params.add('a_bm_1', value=round(random.uniform(0,1),3), min=0, max=1)
        params.add('a_ac_1', min=0, max=1, expr='1-a_bm_1')

        params.add('V_in_2', value=round(random.uniform(0,150),3), min=0, max=150)
        params.add('a_et_2', value=round(random.uniform(0,remain),3), min=0, max=1)
        remain -= params['a_et_2'].value
        params.add('a_bt_2', value=round(random.uniform(0,remain),3), min=0, max=1)
        remain -= params['a_bt_2'].value
        params.add('a_bl_2', value=round(random.uniform(0,remain),3), min=0, max=1)
        params.add('a_ac_2', min=0, max=1, expr='1-a_et_2-a_bt_2-a_bl_2')
        params.add('k_et_2', value=round(random.uniform(0,100),3), min=0, max=100)
        
        params_valid = valid_params(params)

    return params