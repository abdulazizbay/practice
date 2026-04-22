print("=== for operator ===")
# Iterable objects > string dict tuple list range map filter

text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year="2025")
range_obj = range(5)  # [0, 5]

for letter in text:
    print(f"letter:", letter)

print("-----")

for number in numbs:
    print(f"number:", number)

print("-----")

for key in car_obj:
    print(f"the key : {key} => {car_obj.get(key)}")

print("-----")

for x in range(1, 20, 5):
    print("x: ", x)

print("=== break else ===")

for x in range(1, 20, 5):
    print("x: ", x)
    if x > 10:
        print("reached break")
        break
else:
    print("executed succesfully")

print("=== while operator ===")
numb = 40
while numb > 0:
    numb -= 10
    print(f"numb exuals to {numb}")

print("-----")
count = 0
while True:
    count += 1
    x = int(input("Find Number: "))

    if x == 41:
        print(f"you found right num in {count} steps")
        break
    else:
        print("wrong, try again")
