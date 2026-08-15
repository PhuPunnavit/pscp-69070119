"""brickbridge"""

def main():
    """main"""
    a = int(input())
    b = int(input())
    goal = int(input())
    need_b = goal // 5
    big_use = 0
    if b >= need_b:
        big_use = need_b
    else:
        big_use = b

    small_need = goal - (big_use * 5)

    if a >= small_need:
        print(small_need)
    else:
        print(-1)

main()
