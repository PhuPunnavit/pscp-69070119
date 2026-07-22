"""coke"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    sol = d * a
    if not d:
        print(0)
    elif not b:
        print(sol)
    else:
        discount = ((d - 1) // b) * c
        sol3 = d - ((d - 1) // b)
        result = (sol3 * a) + discount
        print(result)

main()
