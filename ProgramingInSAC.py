#This program was a competition between tree stupid boys

print("This program is a dinamic calculator. You can put the numbers and choose the operation that you want to do.")
numbers = []
operations = []
result = 0
j = 0

value = int(input("How many numbers do you want enter?"))
for i in range(value):
    number = float(input("What is the value?"))
    numbers.append(number)

for i in range(0, value):
    j = j + 1
    if i < value:
        operation = str(input(f'What operation do you want to do between the number {j} and the number {j+1}'))
        operations.append(operation)
        if operation == "+":
            continue
        elif operation == "-":
            continue
        elif operation == "*":
            val = numbers[i] * numbers[i+i]
            numbers.pop(i)
            numbers.pop(i+1)
            operations.pop(i)
            numbers.append(result)
            value = value-1
        elif operation == "/":
            val = numbers[i] / numbers[i+1]
            numbers
            numbers.pop(i+1)
            operations.pop(i)
            numbers.append(result)
            value = value-1

for i in range(0, value):
    j = j + 1
    if i < value:
        if operation == "+":
            val = numbers[i] + numbers[j]
            numbers.pop(i)
            numbers.pop(j)
            operations.pop(i)
            numbers.append(result)
            value = value-1
        elif operation == "-":
            val = numbers[i] - numbers[j]
            numbers.pop(i)
            numbers.pop(j)
            operations.pop(i)
            numbers.append(result)
            value = value-1
cout()
