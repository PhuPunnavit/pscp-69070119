"""Align"""

def main():
    """main"""
    size = int(input())
    align = input().strip()
    text = input()

    padding = size - len(text)

    if align == "left":
        print(text + " " * padding)
    elif align == "right":
        print(" " * padding + text)
    elif align == "center":
        pad_left = (padding + 1) // 2
        pad_right = padding // 2
        print(" " * pad_left + text + " " * pad_right)

main()
