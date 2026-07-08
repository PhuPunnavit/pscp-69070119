"""Heron of Alexandria"""
import math as m

val_a = float(input())
val_b = float(input())
val_c = float(input())

while val_a <= 0 and val_b <= 0 and val_c <= 0:
    val_a = float(input())
    val_b = float(input())
    val_c = float(input())

val_s = (val_a + val_b + val_c) / 2
area = m.sqrt(val_s * (val_s - val_a) * (val_s - val_b) * (val_s - val_c))

print(f"{area:.3f}")
