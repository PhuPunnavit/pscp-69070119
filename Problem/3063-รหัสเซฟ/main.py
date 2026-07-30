"""Safe password"""

letters = input()
val_a = int(input())

if letters == "H" and val_a == 4567:
    print("safe unlocked")
elif letters != "H" and val_a == 4567:
    print("safe locked - change char")
elif letters == "H" and val_a != 4567:
    print("safe locked - change digit")
else :
    print("safe locked")
