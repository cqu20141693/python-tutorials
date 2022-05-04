"""
一、 既然多线程可以缩短程序运行时间，那么，是不是线程数量越多越好呢？
显然，并不是，每一个线程的从生成到消亡也是需要时间和资源的，太多的线程会占用过多的系统资源（内存开销，cpu开销），而且生成太多的线程时间也是可观的，很可能会得不偿失，这里给出一个最佳线程数量的计算方式：

最佳线程数的获取：
1、通过用户慢慢递增来进行性能压测，观察QPS（即每秒的响应请求数，也即是最大吞吐能力。），响应时间
2、根据公式计算:服务器端最佳线程数量=((线程等待时间+线程cpu时间)/线程cpu时间) * cpu数量
3、单用户压测，查看CPU的消耗，然后直接乘以百分比，再进行压测，一般这个值的附近应该就是最佳线程数量。

二、为什么要使用线程池？

对于任务数量不断增加的程序，每有一个任务就生成一个线程，最终会导致线程数量的失控，例如，整站爬虫，假设初始只有一个链接a，那么，这个时候只启动一个线程，
运行之后，得到这个链接对应页面上的b，c，d，，，等等新的链接，作为新任务，这个时候，就要为这些新的链接生成新的线程，线程数量暴涨。在之后的运行中，线程数量还会不停的增加，完全无法控制。
所以，对于任务数量不端增加的程序，固定线程数量的线程池是必要的。
"""
import time

import threadpool as threadpool


def sayhello(a):
    print("hello: " + a)
    time.sleep(2)


def testThreadPool():
    """
    测试 threadpool 模块，已经不推荐使用
    :return:
    """
    global result
    seed = ["a", "b", "c"]
    start = time.time()
    task_pool = threadpool.ThreadPool(5)
    requests = threadpool.makeRequests(sayhello, seed)
    for req in requests:
        task_pool.putRequest(req)
    task_pool.wait()
    end = time.time()
    time_m = end - start
    print("time: " + str(time_m))
    start1 = time.time()
    for each in seed:
        sayhello(each)
    end1 = time.time()
    print("time1: " + str(end1 - start1))


from concurrent.futures import ThreadPoolExecutor


def testFuture():
    """
    2、未来：
    使用concurrent.futures模块，这个模块是python3中自带的模块
    :return:
    """
    seed = ["a", "b", "c"]
    start1 = time.time()
    for each in seed:
        sayhello(each)
    end1 = time.time()
    print("time1: " + str(end1 - start1))
    start2 = time.time()
    with ThreadPoolExecutor(3) as executor:
        for each in seed:
            executor.submit(sayhello, each)
    end2 = time.time()
    print("time2: " + str(end2 - start2))
    start3 = time.time()
    with ThreadPoolExecutor(3) as executor1:
        executor1.map(sayhello, seed)
    end3 = time.time()
    print("time3: " + str(end3 - start3))


if __name__ == '__main__':
    testThreadPool()
    print("----- test future ------")
    testFuture()
