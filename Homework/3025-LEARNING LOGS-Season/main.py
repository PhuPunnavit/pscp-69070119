"""Season"""

def main():
    """main function"""

    month = int(input())
    date = int(input())

    
    if month == 1 or 2 and date <= 20:
        print("winter")
    elif month == 3 and date <= 20:
        print("winter")
    elif month == 3 and date >= 21:
        print("spring")
    elif month == 4 or 5 and date <= 20:
        print("spring")
    elif month == 6 and date <= 20:
        print("spring")
    elif month == 6 and date >= 21:
        print("summer")
    elif month == 7 or 8 and date <= 20:
        print("summer")
    elif month == 9 and date <= 20:
        print("summer")
    elif month == 9 and date >= 21:
        print("fall")
    elif month == 10 or 11 and date <= 20:
        print("fall")
    elif month == 12 and date >= 21:
        print("fall")
    else:
        print("winter")

main()
