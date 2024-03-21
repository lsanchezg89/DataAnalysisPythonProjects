import numpy as np

def calculate(list):
    if (len(list) == 9):
        array = np.array(list).reshape(3, 3)
        mean = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)]
        variance = [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array)]
        standard_deviation = [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array)]
        maximum = [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array)]
        minimum = [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array)]
        sum_array = [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array)]
        calculations = {
            'mean': mean,
            'variance': variance,
            'standard deviation': standard_deviation,
            'max': maximum,
            'min': minimum,
            'sum': sum_array
            }
        return calculations
    else:
        raise ValueError("List must contain nine numbers.")