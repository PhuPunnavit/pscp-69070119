"""Temperature"""

def main():
    """main"""
    c = float(input())
    unit_in = input()
    unit_out = input()
    temp_c = 0
    result = 0
    if unit_in == "C":
        temp_c  = c
    elif unit_in == "K":
        temp_c = c - 273.15
    elif unit_in == "F":
        temp_c = (c - 32) / (9/5)
    elif unit_in == "R":
        temp_c = (c - 491.67) * 5 / 9

    if unit_out == "C":
        result = temp_c
    elif unit_out == "K":
        result = temp_c + 273.15
    elif unit_out == "R":
        result = (temp_c + 273.15) * 9/5
    elif unit_out == "F":
        result = temp_c * 9 / 5+32
    print(f"{result:.2f}")
main()
