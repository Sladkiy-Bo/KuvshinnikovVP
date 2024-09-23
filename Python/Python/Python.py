print("Hello!")
print("Enter your numbers:")
x, y = map(int, input().split())
op = input("Yout operation: ")
if op == '+':
    print(x+y)
elif op == '-':
    print(x-y)
elif op == '*':
    print(x*y)
else:
    print(x / y)
