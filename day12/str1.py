
import pyperclip
# 转义字符
print('My brother\'s name is \'007\'')
print(r'My brother \'s name is \'007\'')
str = 'hello123world'

print('he' in str)
print('her' in str)

print(str.isalpha())

print(str.isalnum())

print(str.isdecimal())

print(str[0:5].isalnum())
print(str[5:8].isdecimal())

list = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
print('\n'.join(list))
sentence = 'You go your way I will go mine'

words = sentence.split()

print(words)
email = '     12345@126.COM   '
print(email)
print(email.strip())
print(email.rstrip())

# 将文本放到系统剪贴板中
pyperclip.copy('老虎不发威，你当我是病猫')

