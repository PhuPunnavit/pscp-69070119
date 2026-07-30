"""ค่าน้อยสุด 4 ค่า"""

def main():
    """main"""
    n = int(input())
    mylist = []
    for _ in range(n):
        number = int(input())
        mylist.append(number)
    lowest = mylist[0]
    for number in mylist:
        if number < lowest:
            lowest = number
    print(lowest)

main()
