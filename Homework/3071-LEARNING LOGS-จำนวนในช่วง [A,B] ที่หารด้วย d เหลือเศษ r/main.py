"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

def main():
    """main"""
    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())
    result = 0
    for i in range(A,B+1):
        sum_r = i % d
        if sum_r == r:
            result += 1
    print(result)

main()
