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

print(" === Conditions ===")

x = 5
if x > 5:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("----")
age = 20
# person = None

# if age > 16:
#     person = "adult"
# else:
#     person = "child"
# print(person)

# Ternery operator
person = "adult" if age > 18 else "minor"
print("person: ", person)

print("-----")
is_student = True
is_admin = False
is_guest = False
is_parent = True

if not is_student:
    print("wellcome here, do u want to be a student")
elif is_admin:
    print("please go to this office")
elif is_guest or is_parent:
    print("waiting room is over there")
else:
    print("ETC")
