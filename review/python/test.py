def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())

print(odd())
print(odd())

odd3 = calculate()
print(odd3())
print(odd3())
print(odd3())