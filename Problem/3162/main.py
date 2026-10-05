"""สูตรคูณ"""

def main():
    """main"""
    n = int(input())
    result = 0
    for i in range(1,13):
        result = n * i
        i += 1
        print(f"{n} * {i-1} = {result}")

main()
