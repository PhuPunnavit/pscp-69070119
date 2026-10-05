"""ไพ่ 44 ใบ"""

def main():
    """main"""

    s = input().strip().upper()

    rank_code = s[:-1]
    suit_code = s[-1]
    if rank_code == "A":
        rank = "ace"
    elif rank_code == "J":
        rank = "jack"
    elif rank_code == "Q":
        rank = "queen"
    elif rank_code == "K":
        rank = "king"
    else:
        rank = rank_code
    if suit_code == "D":
        suit = "diamonds"
    elif suit_code == "H":
        suit = "hearts"
    elif suit_code == "S":
        suit = "spades"
    else:
        suit = "clubs"
    print(rank, "of", suit)

main()
