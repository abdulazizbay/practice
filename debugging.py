

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