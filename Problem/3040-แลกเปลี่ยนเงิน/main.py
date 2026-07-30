"""แลกเปลี่ยนเงิน"""

def main():
    """main"""
    total_money = int(input())
    ten_coin = total_money // 10
    left_ten_coin = total_money % 10
    five_coin = left_ten_coin // 5
    left_five_coin = left_ten_coin % 5
    two_coin = left_five_coin // 2
    left_two_coin = left_five_coin % 2
    one_coin = left_two_coin // 1
    print(f"10 = {ten_coin}")
    print(f"5 = {five_coin}")
    print(f"2 = {two_coin}")
    print(f"1 = {one_coin}")

main()
