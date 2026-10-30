
def calculator(method):

    def add(*args):
        return sum(list(args))

    def subtract(first, *args):
        return first - sum(list(args))

    def divide(a, b):
        return a/b

    def multiply(*args):
        values =list(args)
        total = 1
        for number in values:
            total *= number
        return total

    if method == "add":
        return add
    if method == "subtract":
        return subtract
    if method == "divide":
        return divide
    if method == "multiply":
        return multiply

