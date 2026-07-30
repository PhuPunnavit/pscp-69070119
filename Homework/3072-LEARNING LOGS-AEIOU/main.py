"""AEIOU"""

def main():
    """main"""
    text = input()
    textlower = text.lower()
    check_a = 0
    check_e = 0
    check_i = 0
    check_o = 0
    check_u = 0
    for i in textlower:
        if i == "a" :
            check_a += 1
        elif i == "e":
            check_e += 1
        elif i == "i":
            check_i += 1
        elif i == "o":
            check_o += 1
        elif i == "u":
            check_u += 1
        else:
            pass
    if check_a > 0 :
        print(f"a : {check_a}")
    if check_e > 0 :
        print(f"e : {check_e}")
    if check_i > 0 :
        print(f"i : {check_i}")
    if check_o > 0 :
        print(f"o : {check_o}")
    if check_u > 0 :
        print(f"u : {check_u}")
main()
