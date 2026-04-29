from PIL import Image

print("=== python packages and core package ===")

# # core packages - no need for pip install
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(150)

# turtle.done()

print("----")
my_file = open("./material/message.txt", "r")
try:
    content = my_file.read()
    print("content", content)
finally:
    my_file.close()

# with
with open("./material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("ur content:", your_content)

print("Done")

print("=== package manager & external package ===")
'''
    Package managers: pip, pipenv, npm, yarn, composer, brew
'''


# with Image.open("./material/bgImage.jpg") as img_obj:
#     resized_img = img_obj.resize((200, 200))
#     resized_img.show()
#     resized_img.save("./material/sample.png")


print("=== Debugging ===")


def get_summary(*args):
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount # solve the bug via debugging 


result = get_summary(1, 2, 4, 5, 12)
print(result)
