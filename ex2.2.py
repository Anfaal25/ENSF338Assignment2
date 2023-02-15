import sys
import time
import matplotlib.pyplot as plt
import json



sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open('ex2.json', 'r') as f:
    arr = json.load(f)

low = 0
high = len(arr) - 1

func1(arr, low, high)



def time_func1(n):
    arr = list(range(n))
    low = 0
    high = len(arr) - 1
    start_time = time.time()
    func1(arr, low, high)
    end_time = time.time()
    return end_time - start_time

n_values = [10, 100, 1000]
execution_times = []

for n in n_values:
    execution_time = time_func1(n)
    execution_times.append(execution_time)
    print("n = {}, Execution time: {} seconds".format(n, execution_time))

plt.plot(n_values, execution_times)
plt.xlabel("Array Size (n)")
plt.ylabel("Execution Time (s)")
plt.title("QuickSort Execution Time")
plt.show()
