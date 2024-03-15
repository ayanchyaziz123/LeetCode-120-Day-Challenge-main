def subset(start, temp):
    if len(arr) <= start:
        res.append(temp.copy())
        return
    # Include the element at the current index 'start' in the subset
    temp.append(arr[start])
    subset(start + 1, temp)
    
    # Exclude the element at the current index 'start' from the subset
    if temp:  # Check if 'temp' list is not empty before popping
        temp.pop()
    subset(start + 1, temp)

arr = [1, 2, 3, 4]
temp = []
res = []
subset(0, temp)
print(res)
