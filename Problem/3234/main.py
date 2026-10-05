"""ไฟคริสตมาส"""

def main():
    """main"""
    data = input().split()
    start = data[0].upper()
    n = int(data[1])

    if start == "R":
        first = 0
    elif start == "G":
        first = 1
    else:
        first = 2

    result = ""
    for i in range(n):
        now = (first + i) % 3

        if now == 0:
            color = "Red"
        elif now == 1:
            color = "Green"
        else:
            color = "Blue"

        if i == 0:
            result = color
        else:
            result = result + " " + color

    print(result)

main()
