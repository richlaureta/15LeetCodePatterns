character = '*'

starSize: int = int(input("How many level of star(s) do you want to see? "))
increment = 1

for i in range(0, starSize):
    print(character * increment)
    increment += 1
