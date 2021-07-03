import math
import random

def mul(a1, b1, a2, b2, private_key):
    temp1 = b1 * b2
    temp2 = pow(a1, private_key) * pow(a2, private_key)
    result = temp1 / temp2
    return result


def div(a1, b1, a2, b2, private_key):
    temp3 = b1 * pow(a2, private_key)
    temp4 = pow(a1, private_key) * b2

    result = temp3 / temp4
    return result


def add(a1, b1, a2, b2, private_key, generator):
    temp1 = b1 * b2
    temp2 = pow(a1, private_key) * pow(a2, private_key)
    result = temp1 // temp2
    result2 = math.log(result, generator)
    return result2


def sub(a1, b1, a2, b2, private_key, generator):
    temp1 = b1 * pow(a2, private_key)
    temp2 = pow(a1, private_key) * b2

    result = temp1 // temp2
    sub_result = math.log(result, generator)
    return sub_result


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
                                                           for powers in range(1, modulo)}]

if __name__ == '__main__':
    message = 10
    message2 = 10
    print('Massage 1:', message)
    print('Massage 2:', message2)
    result = 0.0
    limited_float = round(result, 2)
    lower = 100
    upper = 200
    list1 = []

    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    list1.append(num)
                    
    prime = (random.choice(list1))

    primitive_roots = primRoots(prime)

    generator = (random.choice(primitive_roots))

    private_key = random.randint(2, prime - 2)

    Y = pow(generator, private_key)

    print("Public_key: (", prime, ",", generator, ",", Y, ")")

    private_key2 = (random.choice(list1))
    private_key3 = (random.choice(list1))

    a1 = (pow(generator, private_key2))
    b1 = (message * pow(Y, private_key2))

    a2 = (pow(generator, private_key3))
    b2 = (message2 * pow(Y, private_key3))

    multiplication = mul(a1, b1, a2, b2, private_key)
    division = div(a1, b1, a2, b2, private_key)

    a1 = (pow(generator, private_key2))
    b1 = (pow(generator, message) * pow(Y, private_key2))

    a2 = (pow(generator, private_key3))
    b2 = (pow(generator, message2) * pow(Y, private_key3))

    addition = add(a1, b1, a2, b2, private_key, generator)
    subtract = sub(a1, b1, a2, b2, private_key, generator)
    
    print('Addition:', addition)
    print('Subtraction:', subtract)
    print('Multiplication:', multiplication)
    print('Division:', division)