n = int(input())
arr = list(map(int, input().split()))

first = float('-inf')
second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print(second if second != float('-inf') else -1)