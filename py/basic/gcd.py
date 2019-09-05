def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(60, 31))
print(gcd(81, 27))


def gcd_2(a, b):
    if b == 0:
        return a
    return gcd_2(b, a % b)


print(gcd_2(1, 5))
print(gcd_2(3, 6))
print(gcd_2(60, 24))
print(gcd_2(60, 31))  # gcd(31, 60 % 31) gcd(29, 31 % 29) gcd(2, 29 % 2) gcd(1, 2 % 1) gcd (1, 0)
print(gcd_2(81, 27))
