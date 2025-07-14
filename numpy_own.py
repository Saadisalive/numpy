import numpy as np

arr_o = np.arange(10)
print(f'orignal array{arr_o}')

arr_m = arr_o.copy()
arr_m[arr_m % 2 != 0] = -1
print(f'array with no odds number {arr_m}')
print(f'orignal array {arr_o}')

arr_d = arr_o.reshape(2, 5)
print(f'two daimansional array \n{arr_d}')

sum_o = 0
for x in arr_o:
    sum_o += x
print(f'sum of all elements in array ({sum_o})')