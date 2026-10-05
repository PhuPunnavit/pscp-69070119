"""โรงแรมกลางกรุง ไม่มีชั้น 13"""

def main():
    """main"""
    n = int(input())
    d1 = n // 10000 % 10
    d2 = n // 1000 % 10
    d3 = n // 100 % 10
    d4 = n // 10 % 10
    d5 = n % 10
    if d1 > 5:
        floor = 9
    elif d2 > 5:
        floor = 10
    elif d3 > 5:
        floor = 11
    elif d4 > 5:
        floor = 12
    elif d5 > 5:
        floor = 14
    else:
        floor = 13

    if d1 == d5 and d2 == d4:
        if d1 + d5 > 5:
            second = 1
        elif d2 * d4 > 5:
            second = 2
        else:
            second = 0
    else:
        if not  d5 == 0 and d1 // d5 > 5:
            second = 1
        elif d2 - d5 > 5:
            second = 2
        else:
            second = 0

    total = d1 + d2 + d3 + d4 + d5
    product = d1 * d2 * d3 * d4 * d5

    if total > 25:
        third = 1
    elif product > 55:
        third = 2
    else:
        third = 0

    print(floor * 100 + second * 10 + third)

main()
