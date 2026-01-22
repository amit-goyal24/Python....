# Largest of Two Numbers
a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)


# Largest Of Three Number
a, b, c = map(int, input("Enter three numbers: ").split())
print("Largest =", max(a, b, c))

