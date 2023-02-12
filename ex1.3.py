#ex1.3


#pre_exist dictionary added to keep a log of values that have already been calculated.
#This prevents time being wasted in re-calculating values for future parts/terms of the sequence.
def func(n, pre_exist={}):
    if n == 0 or n == 1:
        return n
    if n in pre_exist:
        return pre_exist[n]
    pre_exist[n] = func(n-1, pre_exist) + func(n-2, pre_exist)
    return pre_exist[n]
