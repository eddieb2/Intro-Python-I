# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# !! When you use a variable in a function, it's local in scope to the function.  !!
x = 12


def change_x():
    global x  # Allows us to access the global x variable
    print(x)  # 12
    x = 99


change_x()  # 99

# !! This prints 12. What do we have to modify in change_x() to get it to print 99? !!
# Ans: You have to add the global keyword to the function with the variable you want to access.
print(x)


# This nested function has a similar problem.
# WHY DO I HAVE TO HAVE 2 GLOBAL Y'S ?

def outer():
    global y
    y = 120

    def inner():
        global y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()
print(f"y after execution: {y}")
