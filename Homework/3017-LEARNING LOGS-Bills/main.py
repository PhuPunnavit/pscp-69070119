"""Bill"""

Real_Cost = int(input())

Service_Cost = Real_Cost * 0.10

if Service_Cost < 50:
    Service_Cost = 50
elif Service_Cost > 1000:
    Service_Cost = 1000

Before_Vat = Service_Cost + Real_Cost
Result = Before_Vat * 1.07

print(f"{Result:.2f}")
