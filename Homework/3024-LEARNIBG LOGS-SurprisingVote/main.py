"""SurprisingVote"""

def main():
    """main"""
    total_score = float(input())
    max_score = float(input())
    min_score = total_score - 2 * max_score
    if min_score <= 0:
        min_score = 0

    if max_score - min_score > 2 :
        print("Surprising")
    else:
        print("Not surprising")

main()
