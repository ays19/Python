def greater_num(arr):
    count = 0
    for num in arr:
        if num > 10:
            count =count+1
    return count
print(greater_num([4,5,7,9,11,12]))