"""Inflation"""

def main():
    """main"""
    n_input = int(float(input()) *  100)
    k = int(input())
    for _ in range(k):
        n_input += (n_input * 381) // 10000
    x = n_input // 100
    y = n_input % 100
    print(f"{x}.{y:02d}")

main()
    