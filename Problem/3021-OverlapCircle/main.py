"""OverlapCircle0"""
import math as m

def main():
    """main"""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())

    solution1 = m.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
    solution2 = r1 + r2

    if solution1 <= solution2:
        print("overlapping")
    else:
        print("no overlapping")

main()
