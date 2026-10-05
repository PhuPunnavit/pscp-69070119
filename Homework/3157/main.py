"""score game"""

def main():
    """main"""
    n = int(input())
    result = 0
    for _ in range(n):
        x = input()
        if x == "+":
            result += 10
        else:
            result -= 5
    print(result)
main()
