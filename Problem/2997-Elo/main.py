"""Elo"""

val_ra = int(input())
val_rb = int(input())
val_c = input()

EA = 1 / (1 + 10**((val_rb - val_ra) / 400))
EB = 1 / (1 + 10**((val_ra - val_rb) / 400))

if val_c == "A":
    print(f"{EA:.2f}")
else:
    print(f"{EB:.2f}")
