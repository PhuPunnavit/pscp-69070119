"""test"""

def main():
    """main"""
    a = int(input())
    score = []
    for _ in range(a):
        b = int(input())
        score.append(b)
    max_score = max(score)
    print(max_score)
    count_score = score.count(max_score)
    print(count_score)

main()
