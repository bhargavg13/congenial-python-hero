def factorialnum(a):
    if a < 0:
        return print("Error input. Please input a positive integer only.")
    elif isinstance(a, float):
        return print("Error input. Please input a positive integer only.")
    elif a == 0:
        return print(1)
    elif a == 1:
        return print(1)
    else:
        j = a-1
        facto = a
        for x in range(1, j+1):
            facto *= a-x
        return print(facto)


factorialnum(50)
