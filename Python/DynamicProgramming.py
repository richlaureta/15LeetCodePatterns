def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    array = [0] * (n + 1)

    array[0] = 0
    array[1] = 1
    for i in range(2, len(array)):
        array[i] = array[i-2] + array[i-1]

    return array[n]

if __name__ == "__main__":
    print(fib(8))