"""ของขวัญและขโมย"""

def main():
    """main"""
    n, k, t = map(int, input().split())
    t -= 1
    pos = 0
    count = 1
    if pos != t:
        for _ in range(n):
            nxt = (pos + k) % n
            if not nxt:
                break
            count += 1
            pos = nxt
            if pos == t:
                break
    print(count)

main()
