import sys
from fractions import Fraction

def myPow(x: float, n: int) -> float:
    #Problem #5 Pow(x, n)

    # multiply: float = x
    # multiply1: float = float(1)
    # negativeMultiply: float = float(0)
    
    # if x == float(0):
    #     return float(0)
    # else:
    #     negativeMultiply = float(1/x)

    # if n == 0:
    #     return 1
    # elif n == 1:
    #     return x
    # elif n == -1:
    #     return negativeMultiply
    # elif n < 0:
    #     for i in range(0, abs(n)):
    #         multiply1 *= negativeMultiply
    #     return multiply1
    # else:
    return float(x**n)


def main():
    print(myPow(2, -3))

if __name__ == "__main__":
    sys.exit(main())