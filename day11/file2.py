birth = input('请输入你的生日: ')
with open('pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for l in lines:
        pi_string += l.strip()
    if birth in pi_string:
        print('Gingo !')