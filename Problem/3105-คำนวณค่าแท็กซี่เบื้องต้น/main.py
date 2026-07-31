"""คำนวณค่าแท็กซี่เบื้องต้น"""

def main():
    """main"""
    distance = int(input())
    price = 0
    if distance == 1:
        price = 35
    elif 1 < distance <= 10:
        price = (distance - 1) * 5 + 35
    else:
        price = 9 * 5 + (distance - 10) * 8 + 35
    print(price)

main()
