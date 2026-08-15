"""ink"""

import math
def main():
    """main"""
    spread_rate, num_requests = map(int, input().split())
    pi = 3.1416
    for _ in range(num_requests):
        x, y = map(int, input().split())
        r_squared = x**2 + y**2
        area = pi * r_squared
        time_taken = area / spread_rate
        print(math.ceil(time_taken))


main()
