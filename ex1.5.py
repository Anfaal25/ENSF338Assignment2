import time
import matplotlib.pyplot as plt
import numpy as np



def func(n):
    if (n == 0 or n == 1):
        return n
    else:
        return func(n-1) + func(n-2)
    
results = {}

for i in range(36):
    start_time = time.time()
    func(i)
    end_time = time.time()
    results[i] = end_time - start_time
print(results)



def func_imp(m, pre_exist={}):
    if m == 0 or m == 1:
        return m
    if m in pre_exist:
        return pre_exist[m]
    pre_exist[m] = func_imp(m-1, pre_exist) + func_imp(m-2, pre_exist)
    return pre_exist[m]


x = []
y = []
for j in range(36):
    start = time.time()
    func_imp_code = func_imp(j)
    end = time.time()
    x.append(j)
    y.append(end - start)


xaxis = np.array(list(results.keys()))
yaxis = np.array(list(results.values()))



plt.subplot(1,2,1)
plt.plot(xaxis,yaxis)
plt.title("Original Code")
plt.xlabel("Integers")
plt.ylabel("Time")


plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Improved Code")
plt.xlabel("Integers")
plt.ylabel("Time")

plt.show()





