from lmfit import Minimizer, conf_interval
from kinetic_model.get_residuals import get_residuals

def get_confidence_interval (df, result):
    
    data_holder_list = [df]

    minner = Minimizer(get_residuals, result.params, fcn_args = data_holder_list ) # may need to change to args
    #result = minner.leastsq()
    result2 = minner.minimize(method='Nelder')


    return conf_interval(minner, result2)