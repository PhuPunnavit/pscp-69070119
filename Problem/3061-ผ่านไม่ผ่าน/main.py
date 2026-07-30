"""pass / not pass"""

def main():
    """main"""
    midterm = int(input())
    final = int(input())
    sum1 = midterm + final
    if sum1 >= 50:
        print(sum1)
        print("pass")
    else:
        print(sum1)
        print("fail")

main()
