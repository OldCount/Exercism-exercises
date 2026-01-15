def square(number):
    if number > 64:
        raise ValueError("square must be between 1 and 64")
    elif number < 1:
        raise ValueError("square must be between 1 and 64")
    grain = 1
    square = number
    for i in range(number-1):
        grain = grain*2
    return grain
        


def total():
    grain = 1
    total = 1
    for i in range(63):
        grain = grain*2
        total += grain
    return total