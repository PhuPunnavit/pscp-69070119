"""สลับหมายเลข"""

val_a = int(input())
val_b = input()
val_c = str(val_a)
val_d = val_c[::-1]
val_e = int(val_d)
result = ""
if val_b == "+":
    result = val_a + val_e
elif val_b == "*":
    result = val_a * val_e

print(val_a, val_b, val_e, "=", result)
