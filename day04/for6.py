"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""

row = int(input('请输入行数：'))
for i in range(row):
    for _ in range(i +1):
        print('*', end='')
    print()

print()

for i in range(row):
    for j in range(row):
        if j < row - i -1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()

mid = row//2 + 1
for i in range(row):
    if i % 2 == 0:
        continue
    for j in range(row):
        if (mid - (i // 2) -1) <= j and ((i // 2) + mid - 1) >= j:
            print('*',end='')
        else:
            print(' ', end='')
    print()