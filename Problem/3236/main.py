"""รหัสแฝดเทค"""

def main():
    """main"""
    n = int(input())
    a = input().strip()
    b = input().strip()
    bad = 0
    for i in range(n):
        if int(a[i]) + int(b[i]) != 9:
            bad = bad + 1
    if bad == 0:
        print("YES")
    else:
        print("NO", bad)
main()
