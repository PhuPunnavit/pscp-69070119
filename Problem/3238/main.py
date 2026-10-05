"""Elon Musk (X-shape)"""

def main():
    """main"""
    s = input().strip()
    k = s[-1]
    x = int(s[:-1].strip())
    mid = x // 2
    for i in range(x):
        line = ""
        for j in range(x):
            if j == i or j == x - 1 - i:
                if k == "#":
                    line = line + "#"
                else:
                    depth = i
                    if x - 1 - i < depth:
                        depth = x - 1 - i
                    line = line + chr(ord(k) + mid - depth)
            else:
                line = line + "-"
        print(line)

main()
