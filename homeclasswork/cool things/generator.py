# Generators

def myGenerator():
    print("First Time")
    yield 10

    print("Second Time")
    yield 20

    print("Last Time")
    yield 30

gen = myGenerator()
print(next(gen))
print(next(gen))
print(next(gen))
