def find_max(arr):
    max = arr[0]
    for num in arr:
        if num > arr[0]:
            max = num
        return max
print(max([1,2,3,4,5]))