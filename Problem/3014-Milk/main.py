"""Milk"""

def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    milk = d // a
    if not b or not c:
        total_milk = milk
    else:
        caps = milk
        total_milk = milk
        while caps >= b:
            promo = (caps //b)*c
            left_caps = caps % b
            total_milk += promo
            caps = left_caps + promo

    print(total_milk)

main()
