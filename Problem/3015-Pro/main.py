"""Pro"""

x = int(input())
y = int(input())
a = int(input())
z = int(input())

full_groups = z // x
free_people = full_groups * (x - y)
total_cost = z * a - free_people * a

print(total_cost)
