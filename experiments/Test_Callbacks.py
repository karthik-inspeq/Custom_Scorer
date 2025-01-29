def add (a, b):
    return a + b

def isgreater(a, b):
    return a > b

def islesser(a, b):
    return a < b

def execute(callback, a, b):
    return callback(a, b)

if __name__ == "__main__":
    a = 1
    b = 2
    print(execute(add, a, b))
    print(execute(isgreater, a, b))
    print(execute(islesser, a, b))