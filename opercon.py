print("=== Operators ===")

a = 19
b = 5

print("a > b", a > b)
print("a * b", a * b)
print("a / b", a / b)

result = a // b
left = a % b
print(f"result: {result} and left: {left}")

# a = a + 10
a += 10
print("a: ", a)

print("b * b", b ** 2)
print("b*b*b", b**3)

print("=" * 5)

c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)
e = c

print("c = d", c == d)  # only values
print(id(c), id(d), id(e))

print("c is d", c is d)
print("c is e", c is e)
