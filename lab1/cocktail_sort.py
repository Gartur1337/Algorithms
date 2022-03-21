import imp
from os import access
import random
from time import time
from statistics import mean
import numpy
import numpy as np

def create_array(N):
    arr = []
    arr[:] = np.array([random.uniform(-1,1) for i in range(N)])
    return arr

def cocktail_sort(N):
    arr = create_array(N)
    left = 0
    right = N - 1
    control = right
    start_time = time()

    while left < right:
        for i in range(left, right):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                control = i
        right = control

        for i in range (right, left, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                control = i
        left = control
    sort_time = time() - start_time
    return sort_time
    
def calculations(N):
    average = []
    for _ in range(1):
        res = cocktail_sort(N)
        average.append(res)
    print (N, min(average), max(average), mean(average))

def main():
    N = [1000]
    for _ in range(3): N.append(N[-1] * 2)
    for num in N: calculations(num)
    
if __name__ == '__main__':
    main()