'''
异步io asyncio模块
'''

import asyncio
import threading
import time


# @asyncio.coroutine
async def hello():
    print('%s : hello , world!' % threading.current_thread())
    # 休眠不会阻塞主线程，因为使用了异步I/O操作
    # 注意有yield from 才会等待休眠操作执行完成
    # yield from asyncio.sleep(2)
    # asyncio.sleep(1)
    time.sleep(1)
    print('%s : bye~ bye~')
    pass

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
print('game over')
loop.close()