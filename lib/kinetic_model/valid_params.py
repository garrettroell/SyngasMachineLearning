def valid_params(params):
    
    p = params.valuesdict()
    output = (p['a_ac_1'] + p['a_bm_1'] <= 1 and
           p['a_ac_2'] + p['a_et_2'] + p['a_bt_2'] + p['a_bl_2'] <= 1)
           
    return output