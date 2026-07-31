"""สถานะน้ำ"""

def main():
    """main"""
    temp = int(input())
    unit = input()
    unit = unit.lower()
    if unit == "f":
        if temp <= 32:
            print("solid")
        elif 32 < temp < 212:
            print("liquid")
        else:
            print("gas")
    else :
        if temp <= 0:
            print("solid")
        elif 0 < temp < 100 :
            print("liquid")
        else :
            print("gas")

main()
