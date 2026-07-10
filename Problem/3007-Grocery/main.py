"""Grocery"""

val_a = input()
val_a_split = val_a.split(" ")

num_a = int(val_a_split[0])
num_b = int(val_a_split[1])    
num_c = int(val_a_split[2])

carrot = (num_a) * 10
cabbage = (num_b) * 25
tomato = (num_c) * 3
result = carrot + cabbage + tomato
print(result)
