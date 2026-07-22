"""ตัวเลขที่หาร 10 ลงตัว"""

def main():
    """main"""
    n = int(input())
    solution_1 = n // 10
    solution_2 = solution_1 * 10
    list_of_number = []
    while solution_2 >= 0:
        list_of_number.append(solution_2)
        solution_2 -= 10
    print(*list_of_number)
main()
