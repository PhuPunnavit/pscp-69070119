"""กระต่ายน้อยล้อมรั้วลวดหนาม"""

w, h, l = map(int, input().split())
price_per_meter = int(input())
fence_length = (w * 2 + h * 2) * l
fence_price = price_per_meter * fence_length
print(fence_length)
print(fence_price)
