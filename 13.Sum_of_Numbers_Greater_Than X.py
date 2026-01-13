x = int(input())
n = int(input())
arr = list(map(int, input().split()))
total = 0
for num in arr:
    if num > x:
        total += num
print(total)