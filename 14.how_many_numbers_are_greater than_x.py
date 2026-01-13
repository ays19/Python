x = int(input())
n= int(input())
arr= list(map(int, input().split()))
count = 0
for num in arr:
    if num > 10:
        count+=1

print(count)        