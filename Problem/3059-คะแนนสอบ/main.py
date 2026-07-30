"""score"""

def main():
    """main"""
    exercise_scored = int(input())
    midterm_test_score = int(input())
    final_score = int(input())

    if exercise_scored >= 5 and midterm_test_score >= 20 and final_score >= 25:
        print("pass")
    else:
        print("fail")

main()
