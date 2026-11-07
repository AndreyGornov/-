def quicksort(arr):
    if len(arr) < 2:
        return arr
    flag = len(arr) // 2
    arr1 = [el for el in arr if el < arr[flag]]
    arr2 = [el for el in arr if el > arr[flag]]
    arr3 = [el for el in arr if el == arr[flag]]
    return quicksort(arr1) + arr3 + quicksort(arr2)

print(quicksort([10,9,8,7]))