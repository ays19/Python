x = int(input())
arr = list(map(int, input().split()))
k = int(input())

k= k%x

rotate = arr[k:] + arr[:k]

print(rotate)
print(*rotate)