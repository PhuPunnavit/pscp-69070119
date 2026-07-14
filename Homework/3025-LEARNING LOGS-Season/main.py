"""season"""

def main():
    """this is the main function"""
    month = int(input())
    date = int(input())

    winter = [1, 2, 3]
    spring = [4, 5, 6]
    summer = [7, 8, 9]
    fall = [10, 11, 12]

    if month in winter:
        pre_result = "winter"
    elif month in spring:
        pre_result = "spring"
    elif month in summer:
        pre_result = "summer"
    elif month in fall:
        pre_result = "fall"
    else:
        pre_result = ""

    if date >= 21 and pre_result == "winter" and not month % 3:
        result = "spring"
        print(result)
    elif date >= 21 and pre_result == "spring" and not month % 3:
        result = "summer"
        print(result)
    elif date >= 21 and pre_result == "summer" and not month % 3:
        result = "fall"
        print(result)
    elif date >= 21 and pre_result == "fall" and not month % 3:
        result = "winter"
        print(result)
    else:
        print(pre_result)

main()
