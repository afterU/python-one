'''
任何时候当你的程序中存在高度重复(或者是通过剪切复制)的代码时，都应该想想是否有更好的解决方案。
在Python当中，通常都可以通过元编程来解决这类问题。 简而言之，元编程就是关于创建操作源代码(比如修改、生成或包装原来的代码)的函数和类。
 主要技术是使用装饰器、类装饰器和元类。不过还有一些其他技术， 包括签名对象、使用 exec() 执行代码以及对内部函数和类的反射技术等。
 本章的主要目的是向大家介绍这些元编程技术，并且给出实例来演示它们是怎样定制化你的源代码行为的。
'''

# 1. 在函数上添加包装器
    # 一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数,
    # 内置的装饰器比如 @staticmethod, @classmethod,@property 原理也是一样的。
    # 需要强调的是装饰器并不会修改原始函数的参数签名以及返回值。 使用 *args 和 **kwargs 目的就是确保任何参数都能适用。
    # 而返回结果值基本都是调用原始函数 func(*args, **kwargs) 的返回结果，其中func就是原始函数。
# 1）定义包装器
import time
from functools import wraps


def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper
# 2） 使用包装器
@timethis
def countdown(n):
    while n > 0:
        n -= 1
        print(n)

countdown(1000)
countdown(10000)

# 例子：用装饰器来实现单例模式。
# from functools import wraps
def singleton(cls):
    instance = {}
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]


@singleton
class President():
    """总统(单例类)"""
    pass
# 说明：上面的代码中用到了闭包（closure），不知道你是否已经意识到了。还没有一个小问题就是，上面的代码并没有实现线程安全的单例，如果要实现线程安全的单例应该怎么做呢？
# from functools import wraps
from threading import Lock
def singleton(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

# 2)  创建装饰器时，保留函数元信息
    # 在编写装饰器的时候复制元信息是一个非常重要的部分。如果你忘记了使用 @wraps ， 那么你会发现被装饰函数丢失了所有有用的信息
print(countdown.__name__)
    # @wraps 有一个重要特征是它能让你通过属性 __wrapped__ 直接访问被包装函数
countdown.__wrapped__(10)

# 3) 解除装饰器
    # 一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函数
    # 可以通过访问 __wrapped__ 属性来访问原始函数， 直接访问未包装的原始函数在调试、内省和其他函数操作时是很有用的
    # 如果有多个包装器，那么访问 __wrapped__ 属性的行为是不可预知的，应该避免这样做
# 4) 定义带参数的装饰器
    # 定义一个可以记录日志的装饰器
import logging

def logged(name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorat(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        log.level = logging.INFO
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.info(logmsg)
            print(logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorat

# Example use
@logged(name='test', message='日志')
def add(x, y):
    return x + y

add(1, 3)

# 装饰器类似于函数的嵌套调用
print("----------")
def func1(a, b):
    c = a + b
    def innerFunc(a, b, d):
        return a + b + d + c
    return innerFunc
print(func1(10, 20)(30, 40, 50))


print("--------------")
def outterFunc(a, b, c):
    return a + b + c
def logg():
    print("outterFunc 执行了")
    return outterFunc
print(logg()(1, 2, 3))

# 5) 可自定义属性的装饰器
from functools import wraps, partial
def attach_wrapper(obj, func= None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged2(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            print(logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal  level
            level = newlevel
        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate

# @logged2(logging.DEBUG)
# def add2(x, y):
#     return x + y

@logged2(logging.CRITICAL, message="example")
def spam():
    print("spam runed")

print("************")
logging.basicConfig(level=logging.DEBUG)
spam()
spam.set_message('Add called')
spam()

# 5) 带可选参数的装饰器







