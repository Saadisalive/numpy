import numpy as np
arr_original = np.arange(10)
print(f"Original array: {arr_original}")

arr_modified = arr_original.copy()
arr_modified[arr_modified % 2 != 0] = -1
print(f"Array with odd numbers replaced: {arr_modified}")
print(f"Original array (unchanged): {arr_original}")

arr_2d = arr_original.reshape(2, 5) # Assuming 10 elements can be reshaped into 2 rows and 5 columns
print(f"2-dimensional array: \n{arr_2d}")

total_sum = 0
for x in arr_original:
    total_sum += x
print(f"Sum of all elements in the original array: {total_sum}")