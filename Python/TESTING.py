import sys

numbers = 19
modulos = numbers
sum = 0

seen = set()

while sum != 1:
    sum = 0
    while numbers > 0:
        modulos = numbers % 10
        numbers = numbers // 10

        sum += modulos * modulos

    numbers = sum
    if numbers in seen:
        print("False")
        sys.exit()
        
    seen.add(numbers)
print("True")

print(digits)