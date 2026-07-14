"""Quadrant"""

VAL_A = int(input())
VAL_B = int(input())

if VAL_A > 0 and VAL_B > 0:
    print("Q1")
elif VAL_A < 0 < VAL_B:
    print("Q2")
elif VAL_A < 0 and VAL_B < 0:
    print("Q3")
elif VAL_B < 0 < VAL_A:
    print("Q4")
elif not VAL_A and VAL_B:
    print("Y")
elif VAL_A and not VAL_B:
    print("X")
else:
    print("O")
