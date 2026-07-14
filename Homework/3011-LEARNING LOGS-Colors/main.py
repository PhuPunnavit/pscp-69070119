"""Color"""

fcolor = input()
Scolor = input()

main_color = ["Red", "Yellow", "Blue"]

if fcolor in main_color and Scolor in main_color:
    if  fcolor == Scolor:
        print(fcolor)
    elif ((fcolor == "Red" and Scolor == "Yellow") or (fcolor == "Yellow" and Scolor == "Red")):
        print("Orange")
    elif  ((fcolor == "Red" and Scolor == "Blue") or (fcolor == "Blue" and Scolor == "Red")):
        print("Violet")
    elif ((fcolor == "Blue" and Scolor == "Yellow") or (fcolor == "Yellow" and Scolor == "Blue")):
        print("Green")
    else:
        print("Error")
else :
    print("Error")
