
print("=== Iterable Objects And Range ===")
# Iterable objects => string dict tuple list range map filter

range_obj = range(3)
print("range_obj:", range_obj)
for letter in "MIT":
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")

print("=== Dictionary ===")
# Dictionary is JSON object

person = {"name": "Abdulaziz", "age": 33, "isSingle":  True}
person_obj = dict(name="Abdulaziz", age=33, isSingle=True)

print(person)
print(person_obj)

# name = person_obj["name"]

# method get()
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"name: {name}, hobby: {hobby}, balance: {balance}")

del person_obj["isSingle"]
for key in person_obj:
    print(f"key: {key} => value: {person_obj[key]}")
