arr = [1,2,0,4,0]
last = 0
for i in range(5):
    if arr[i]:
      arr[last] = arr[i]
      last += 1

for i in range(last, 5):
    arr[i] = 0

print(arr)