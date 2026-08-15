"""AR TIKTOK"""

def main():
    """main"""
    r, x, y = map(int, input().split())

    point_dist_sq = x**2 + y**2
    radius_sq = r**2

    if point_dist_sq < radius_sq:
        print("IN")
    elif point_dist_sq == radius_sq:
        print("ON")
    else:
        print("OUT")


main()
