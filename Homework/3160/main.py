"""prime"""


def main():
    """main"""
    a = int(input())
    b = int(input())

    ans = ""
    count = 0

    for n in range(a, b + 1):
        if n < 2:
            continue

        is_prime = True
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                is_prime = False
                break

        if is_prime:
            ans = ans + str(n) + " "
            count = count + 1

    print(ans.strip())
    print(count)


main()
