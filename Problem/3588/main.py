"""GCD_N"""

def main():
    """main"""
    n = int(input())
    ans = int(input())

    for _ in range(n - 1):
        num = int(input())
        a = ans
        b = num
        for _ in range(100):
            if not b:
                break
            temp = a % b
            a = b
            b = temp
        ans = a

    print(ans)

main()
