"""bonus"""

def main():
    """main"""
    Position, Year, Money = input().split()
    Year = int(Year)
    Money = int(Money)
    result = 0
    if Position == "M":
        result += 1500
    elif Position == "B":
        result += 1000
    else:
        result += 500
    if Position == "M":
        if Year < 5:
            solution = Money * (6 / 100)
            result += solution
        elif Year < 10:
            solution = Money * (8 / 100)
            result += solution
        else:
            solution = Money * (10 /100)
            result += solution
    elif Position == "B":
            if Year < 5:
                solution = Money * (5 / 100)
                result += solution
            elif Year < 10:
                solution = Money * (6 / 100)
                result += solution
            else:
                solution = Money * (7 /100)
                result += solution
    else:
        if Year < 5:
            solution = Money * (4 / 100)
            result += solution
        elif Year < 10:
            solution = Money * (5 / 100)
            result += solution
        else:
            solution = Money * (6 /100)
            result += solution
    print(int(result))

main()
