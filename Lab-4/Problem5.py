
N = int(input("Enter the limit N: "))

a = 0
b = 1

while a < N:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
