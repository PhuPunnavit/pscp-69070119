"""ticket price"""

def main():
    """main"""
    age = int(input())
    status = input()
    if age < 18 or status == "S" or status == "s":
        print("20")
    else:
        print("50")

main()
