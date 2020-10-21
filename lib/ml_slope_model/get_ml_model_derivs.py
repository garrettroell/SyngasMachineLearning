import numpy as np

def get_ml_model_derivs(t, y, gas_comp, ml_model):

    dy = []
    for counter,conc in enumerate(y,0):
        if conc < 0:
            y[counter] = 0
    ml_input = np.concatenate((gas_comp,y)).reshape(1, -1)

    for slope in ml_model.predict(ml_input)[0]:
        if slope > 100:
            slope = 100
        if slope < -100:
            slope = -100
        dy.append(slope)
        
    return dy 