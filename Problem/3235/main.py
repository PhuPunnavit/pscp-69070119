"""กระต่ายอ้วน"""

def main():
    """main"""
    n = int(input())
    over = 0
    max_weight = -1
    max_name = ""
    for _ in range(n):
        data = input().split()
        name = data[0]
        weight = int(data[1])
        if weight > 15:
            over = over + 1
        if weight > max_weight:
            max_weight = weight
            max_name = name

    print(over)
    print(max_name)

main()
