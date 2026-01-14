n = int(input())
arr = list(map(int, input().split()))
target = int(input())

found = False
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[2]== target:
            found = True
            break
    if found:
        break

print("YES" if found else "NO")