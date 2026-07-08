"""password"""

name = input()
surname = input()
age = input()

if len(name) >= 5 and len(surname) >= 5 :
    print(f"{name[0:2]}{surname[:-2:-1]}{age[1:2]}")
else:
    print(f"{name[0:1]}{age}{surname[:-2:-1]}")
