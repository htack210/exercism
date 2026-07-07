def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number - 1)


def total():
    runtot = 0
    
    for number in range(64):
        runtot = runtot + square(number + 1)
    return runtot