'''
找出列表中最大或者最小的元素
'''

def main():
    fruits = ['grape','apple','strawberry','waxberry','pitaya']
    # 直接使用内置max和min函数找出列表中最大和最小元素
    print(max(fruits))
    print(min(fruits))

    max_value = min_value = fruits[0]
    for i in range(1,len(fruits)):
        if fruits[i] > max_value:
            max_value = fruits[i]
        elif fruits[i] < min_value:
            min_value = fruits[i]
    print(max_value)
    print(min_value)

if __name__ == '__main__':
    main()