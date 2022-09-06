input_again = True

while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%D / %d = %f' % (a, b, a/b))
        input_again = False
    except (ValueError, ZeroDivisionError) as msg:
        print(msg)