import numpy as np


def compute_prob(nTrials, numObserved):
    arr=[]
    count=0
    for i in range(1000):
        arr.append(np.random.binomial(nTrials, 0.5))
    for j in arr:
        if j==numObserved:
            count += 1

    return count/len(arr)





