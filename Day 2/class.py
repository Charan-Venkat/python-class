print("Assign muitiple values to multiple variables")
num1, num2, num3 = 10,20 ,30
print("number1 values num1")
print("number1 value", num1)
print("number2 value", num2)
print("number value ", num3)
print("All variable refferences are:", id(num1), id (num2), id(num3))


print("Assign single values to multiple variables")
num1, num2, num3 = 257,257 ,257
print("number1 values num1")
print("number1 value", num1)
print("number2 value", num2)
print("number value ", num3)
print("All variable refferences are:", id(num1), id (num2), id(num3))


print("swapping two numbers")
a, b =10, 20
print("Before swapping")
print(a, b, id(a), id(b))
a, b = b, a
print(a, b, id(a), id(b))



