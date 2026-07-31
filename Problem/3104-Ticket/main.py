"""ticket"""

def main():
    """main"""
    year, day = input().split()
    year = int(year)
    ticket_price = 0

    if day == "Wed":
        if year < 5:
            ticket_price = 0
        elif year <= 18:
            ticket_price = 50
        else:
            ticket_price = 75
    else:
        if year < 5:
            ticket_price = 0
        elif year <= 18:
            ticket_price = 100
        else:
            ticket_price = 150
    print(ticket_price)

main()
