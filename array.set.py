from array import array

print(" ==== array ===")
numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1)", numbers)

numbers.append(100)
numbers.insert(0, 14)
print("numbers(2): ", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3): ", numbers)

del numbers[0:2]
print("numbers(4): ", numbers)


print(" ==== set ===")
# {set} of unique collection without keeping order
new_numbers = array("i", [1, 4, 5, 7, 8, 41])
nums_set = set(new_numbers)

nums_set.add(200)
print(nums_set)

print(" ==== Specific Operators ===")
a = {10, 20, 50}
b = {20, 40}

res1 = a | b  # union
res2 = a & b  # intersection
res3 = a - b  # difference
res4 = a ^ b  # symetric defference

print("res1", res1) # {50, 20, 40, 10}
print("res2", res2) # {20}
print("res3", res3) # {10, 50}
print("res4", res4) # {40, 10, 50}
