"""
利用while实现0~100间的偶数求和
"""

sum = 0
num = 0
while num <= 100:
    sum += num
    num += 2
print(sum)