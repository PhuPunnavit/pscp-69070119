"""หาระยะทางระหว่างจุด 3D"""
import math as m
x1, y1, z1 = map(int, input().split())
x2, y2, z2 = map(int, input().split())

d = m.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

if d.is_integer():
    print(int(d))
else:
    print(f"{d:.2f}")
