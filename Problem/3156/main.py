"""conan"""

def main():
    """main"""
    s = input()
    k = int(input()) % 26
    ans = ""

    for ch in s:
        if 'a' <= ch <= 'z':
            ans = ans + chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        else:
            ans = ans + ch

    print(ans)


main()
