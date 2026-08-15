"""pot"""


def main():
    """main"""
    first_line = input().split()
    n = int(first_line[0])
    k = int(first_line[1])

    counts = [0] * (k + 1)
    for _ in range(n):
        queue_num = int(input())
        counts[queue_num] += 1

    min_people = min(counts[1:])
    remaining = n - (min_people * k)

    print(remaining)

main()
