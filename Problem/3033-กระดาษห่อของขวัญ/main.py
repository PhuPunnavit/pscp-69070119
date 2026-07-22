"""กระดาษห่อของขวัญ"""

def main():
    """main"""
    size = input().split()
    a = float(size[0])
    b = float(size[1])
    c = float(size[2])
    pi = 3.14
    width = 2 * pi  * a + c
    lenght = b + (2 * a)
    print(f"{lenght:.2f} {width:.2f}")

main()
