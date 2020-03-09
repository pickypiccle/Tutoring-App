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



print(compute_prob(30,22))




#Alternative approach
import scipy.stats
def compute_prob2(nTrials, numObserved):
    return scipy.stats.binom.pmf(22,30,0.5)


