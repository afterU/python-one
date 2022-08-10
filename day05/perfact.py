'''
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

'''
import math
import time

start = time.time()
count = 0
for i in range(1,10000):
    sum = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)
        count += 1

# for num in range(1, 10000):
#     sum = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             sum += factor
#             if factor > 1 and num / factor != factor:
#                 sum += num / factor
#     if sum == num:
#         count += 1
#         print(num)
print(count)

end = time.time()
print('执行时间：',(end - start), "秒")