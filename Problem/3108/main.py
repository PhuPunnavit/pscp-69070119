"""promotion"""

def main():
    """main"""
    a, b, c = map(int, input().split())
    price_a = 25
    price_b = 40
    price_c = 55
    total = (a * price_a) + (b * price_b) + (c * price_c)
    if a + b + c >= 3:
        total = int(total * 0.9)
    print(total)

main()
