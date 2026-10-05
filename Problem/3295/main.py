"""Electric_Using"""
import math

def main():
    """Electric_Using"""
    n = int(input())
    tiers = [(10, 5), (40, 7), (50, 10), (100, 12)]
    energy = 0
    rem = n
    for width, rate in tiers:
        used = min(rem, width)
        energy += used * rate
        rem -= used
    energy += rem * 15
    vat = energy * 0.07
    ft_cost = n * 0.5
    total = math.floor((energy + vat + ft_cost) * 10 + 0.5) / 10
    print(total)


if __name__ == "__main__":
    main()
