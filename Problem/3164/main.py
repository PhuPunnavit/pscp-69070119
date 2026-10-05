"""ผลรวมของค่าที่มากกว่า"""

def main():
    """main"""
    n = int(input())
    total = 0
    equation = ""

    for i in range(n):
        a = int(input())
        b = int(input())
        
        if a > b:
            max_val = a
        else:
            max_val = b
            
        total += max_val
        equation += str(max_val)
        
        if i < n - 1:
            equation += " + "

    if n == 1:
        print(total)
    else:
        print(f"{equation} = {total}")

main()