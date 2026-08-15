"""count a e i o u """

def main():
    """main"""
    text = input()
    my_list = ["a", "e", "i", "o", "u"]
    count = 0
    for i in text:
        if i in my_list:
            count += 1
    print(count)

main()
