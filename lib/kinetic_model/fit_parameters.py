from kinetic_model.get_rand_params import get_rand_params
from kinetic_model.get_residuals import get_residuals
from lmfit import Minimizer

def fit_parameters (df):
    print('inside fit parameters')
    data_holder_list = [df]
    
    params = get_rand_params()
    print('ran get rand params')
    minner = Minimizer(get_residuals, params, fcn_args = data_holder_list ) # may need to change to args
    #result = minner.leastsq()
    result = minner.minimize(method='Nelder')
    print('finished fit params')
    return result