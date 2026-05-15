print('My Assignment for Github')
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(add(10, 5))       # Output: 15
print(subtract(10, 5))  # Output: 5
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a + b
