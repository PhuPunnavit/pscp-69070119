"""symbol"""

def main():
    """main"""
    n = int(input())
    for i in range(n):
        i += 1
        if not i % 5 :
            print("X", end="")
        else:
            print("*", end="")

main()
