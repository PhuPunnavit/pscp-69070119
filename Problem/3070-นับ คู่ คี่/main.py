"""even and odd"""

def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    even = 0
    odd = 0

    if not a % 2 :
        even += 1
    else:
        odd += 1
    if not b % 2 :
        even += 1
    else:
        odd += 1
    if not c % 2 :
        even += 1
    else:
        odd += 1
    print(even)
    print(odd)

main()
