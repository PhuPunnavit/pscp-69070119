"""เดินเล่นในงานเทศกาล"""

def main():
    """main"""
    commands = input()
    x = 0
    y = 0
    for move in commands:
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
    if x > 0:
        dist_x = x
    else:
        dist_x = -x
        
    if y > 0:
        dist_y = y
    else:
        dist_y = -y    
    d = dist_x + dist_y
    print(f"{x} {y} {d}")

main()
