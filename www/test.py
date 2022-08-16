# import time
# import uuid

# print(len(uuid.uuid4().hex)) #%s000

# print('%016d' % (int(time.time()*1000),))
# print('%015d' % (int(time.time()*1000),))
# print('%s0000' % (uuid.uuid4().hex,))


# import orm
# import asyncio
# from models import User, Blog, Comment
# 这部分源码来自 https://aodabo.tech/blog/001546713871394a2814d2c180b4e6f8d30c62a3eaf218a000
# async def test(loop):                      # *** 注意此处的密码填自己设的密码 ***
    # await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    #                                        # *** 注意此处的密码填自己设的密码 ***
    # u = User(name='Test', email='test@qq.com1', passwd='1234567890', image='about:blank')
    # await u.save()
    ## 网友指出添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
#     orm.__pool.close()
#     await orm.__pool.wait_closed()
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(test(loop))
#     loop.close()

# 第五步：在 sql 命令行里输入 'SELECT * FROM users;'  然后回车（别漏了分号）
# 显示 test@qq.com 代表测试成功了

# import orm
# from models import User, Blog, Comment

# def test():
#     yield from orm.create_pool(user='www-data', password='www-data', database='awesome')

#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

#     yield from u.save()

# for x in test():
#     pass


# import argparse
# parser = argparse.ArgumentParser(
#     prog= 'top',
#     description='Show top lines from each file'
# )
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-1', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)
# print('-----------')
# print(dir('orm.py'))

# import inspect
# def test(a,b):
#     pass

# print(inspect.signature(test).parameters)

# import functools
# def get(path):      
#     '''
#     Define decorator @get('/path')
#     '''
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             return func(*args, **kw)
#         wrapper.__method__ = 'GET'
#         wrapper.__route__ = path
#         return wrapper
#     return decorator
# @get('test')
# def test():
#     print('abc')

# test()
# import os
# filename = os.path.abspath(__file__)
# print(filename)
# abspath = os.path.dirname(filename)
# print(abspath)
# path = os.path.join(abspath, 'static')
# print(path)

# filename = os.path.abspath('.')
# print(filename)

# print(type(u'abs'))
# print('{:n}'.format(1234))
# print('{:6}'.format(1234))
# print('{:3}'.format(1234))
# print('{:1}'.format(1234))

# import os
# path = os.path.abspath('.')
# print(path)

# https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fup.enterdesk.com%2Fedpic_source%2Fd1%2F27%2F08%2Fd12708c40b84cb8a08c08dfd1f6e11ba.jpg&refer=http%3A%2F%2Fup.enterdesk.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662708061&t=311e5540f61ee1d4c6bf8309e6d922e4
# import mysql.connector

# conn = mysql.connector.connect(user='root', password='xin6934101', database='awesome')
# cursor = conn.cursor()

# cursor.execute('update comments set user_image=%s', ("https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fup.enterdesk.com%2Fedpic_source%2Fd1%2F27%2F08%2Fd12708c40b84cb8a08c08dfd1f6e11ba.jpg&refer=http%3A%2F%2Fup.enterdesk.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662708061&t=311e5540f61ee1d4c6bf8309e6d922e4",))
# values = cursor.fetchall()
# print(values)
# print(cursor.rowcount)
# conn.commit()
# cursor.close()
# conn.close()


import sys


print(sys.byteorder)
