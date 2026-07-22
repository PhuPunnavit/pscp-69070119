"""calculator"""

n = int(input())

def main():
    """main"""

    result = 0
    pre_result = 0
    if n == 1:
        result = 1
    elif n > 1:
        for i in range(1, n + 1):
            pre_result += len(str(i))
    result = pre_result + n
    print(result)

main()
