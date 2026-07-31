"""aeiou"""

def main():
    """main"""
    n = int(input())
    mylist = ["A" , "E" , "I" , "O" , "U"]
    result = 0
    for _ in range (n):
        letters = input()
        if letters in mylist:
            result += 1
    print(result)

main()
