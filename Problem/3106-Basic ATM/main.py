
def main():
    """main"""
    money = int(input())

    if money < 100 or money > 20000 or money % 100:
        print("ERROR")
        return

    thousand = money // 1000
    left_thousand = money % 1000

    fivehundred = left_thousand // 500
    left_fivehundred = left_thousand % 500

    onehundred = left_fivehundred // 100

    if thousand > 0:
            print(f"1000 = {thousand}")
    if fivehundred > 0:
            print(f"500 = {fivehundred}")
    if onehundred > 0:
            print(f"100 = {onehundred}")

    main()
