# array Test

# empty array
arr = [] 

# init with values (can contain mixed types)
arr = [1, "eels"]

# get item by index (can be negative to access end of array)
arr = [1, 2, 3, 4, 5, 6]
arr[0]  # 1
arr[-1] # 6

# get length
length = len(arr)

# supports append and insert
arr.append(8)
arr.insert(6,7)

print arr[0]
print arr[1]
print arr[7]