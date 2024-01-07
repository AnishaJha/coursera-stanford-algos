import math


def recursive_mult1(num1: int, num2: int):
    if abs(num1) < 10 and abs(num2) < 10:
        return num1 * num2
    num1_len = len(str(num1))
    num2_len = len(str(num2))
    n1 = math.ceil(num1_len / 2)
    a = num1 // 10 ** n1
    b = num1 - a * (10 ** n1)
    n2 = math.ceil(num2_len / 2)
    c = num2 // 10 ** n2
    d = num2 - c * (10 ** n2)
    first = recursive_mult1(a, c)
    second = recursive_mult1(a, d)
    third = recursive_mult1(b, c)
    fourth = recursive_mult1(b, d)
    return first * (10 ** (n1 + n2)) + second * (10 ** n1) + third * (10 ** n2) + fourth


print(recursive_mult1(20000, 2554))
print(recursive_mult1(3141592653589793238462643383279502884197169399375105820974944592,
                      2718281828459045235360287471352662497757247093699959574966967627))
