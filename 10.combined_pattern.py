n= int(input())
arr = list(map(int,(input().split())))
total =0
for num in arr:
    if num > 5:
        total += num

print(total)


