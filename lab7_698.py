def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

while True:
    a, b = map(int, input("Enter two numbers: ").split())
    if a == 0 and b == 0:
        break
    print(power(a, b))