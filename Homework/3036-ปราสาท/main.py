"""ปราสาท"""
import math


def main():
    """main"""
    N = int(input())

    if N == 1:
        print(0)
    else:
        r = math.ceil(math.sqrt(N))
        c = N - (r - 1) ** 2
        if c % 2:
            print(2 * (r - 1))
        else:
            print(2 * (r - 1) - 1)

main()
