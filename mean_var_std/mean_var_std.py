# boilerplate-mean-variance-standard-deviation-calculator

import numpy as np

def calculate(list):
    try:
        if len(list) != 9:
            raise ValueError("List must contain nine numbers.")
            
        array_obj = np.array(list)
        array_reshaped = np.reshape(list,(3,3))
        calculations = {
                        'mean': [(np.mean(array_reshaped, axis=0)).tolist(), (np.mean(array_reshaped, axis=1)).tolist(),np.mean(array_obj)],
                        'variance': [(np.var(array_reshaped, axis=0)).tolist(), (np.var(array_reshaped, axis=1)).tolist(),np.var(array_obj)],
                        'standard deviation': [(np.std(array_reshaped, axis=0)).tolist(), (np.std(array_reshaped, axis=1)).tolist(),np.std(array_obj)],
                        'max': [(np.max(array_reshaped, axis=0)).tolist(), (np.max(array_reshaped, axis=1)).tolist(),np.max(array_obj)],
                        'min': [(np.min(array_reshaped, axis=0)).tolist(), (np.min(array_reshaped, axis=1)).tolist(),np.min(array_obj)],
                        'sum': [(np.sum(array_reshaped, axis=0)).tolist(), (np.sum(array_reshaped, axis=1)).tolist(),np.sum(array_obj)]
                     }
        return calculations

    except ValueError as ve :
        raise ve
