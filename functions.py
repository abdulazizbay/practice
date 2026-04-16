''' Functions 
    (1) Define and Call
    (2) Parametr va Argument
    (3) Keyword and default Arguments
    (4) Scope
'''

print("===== Define(parametr) and Call(argument) =====")
# Built-in funtion => print() type()
# Function - reusable block of code
# instead of block {} in Java, Python uses indentation

# define - parametr


def greet(a):
    print(f"how do u do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi, {b}"


# Call - argument
result = greet("abu")
print("result: ", result)

result2 = greeting("abu")
print("result2: ", result2)
