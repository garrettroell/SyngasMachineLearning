def get_kinetic_model_derivs(t,y,params):
    
    p=params.valuesdict()
    dy=[]
    
    if t <= p['t_switch']:
        dy.append(p['V_in_1']      *    p['a_ac_1'] * y[1]) #acetate
        dy.append(p['V_in_1']*(1/20.83)*p['a_bm_1'] * y[1]) #biomass
        dy.append(0)              #butanol
        dy.append(0)              #butyrate
        dy.append(0)              #ethanol
    else:
        dy.append(p['V_in_2']     *     p['a_ac_2'] * y[1] - p['k_et_2']  * y[0] * y[1])
        dy.append(0)
        dy.append(p['V_in_2'] * (1/2) * p['a_bl_2'] * y[1])
        dy.append(p['V_in_2'] * (1/2) * p['a_bt_2'] * y[1])
        dy.append(p['V_in_2']     *     p['a_et_2'] * y[1] + p['k_et_2']  * y[0] * y[1])
        
    return dy