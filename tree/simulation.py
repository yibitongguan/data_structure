# encoding:utf-8

"""
通用的离散事件模拟器
"""
from prioQueue_heap import PrioQueue

class Simulation:
    def __init__(self, duration):
        self._eventq = PrioQueue()  # 事件队列
        self._time = 0              # 当前时间
        self._duration = duration   # 总时长
        
    def run(self):
        while not self._eventq.is_empty():  # 模拟到事件队列空
            event = self._eventq.dequeue()
            self._time = event.time()        # 事件的时间就是当前时间
            if self._time > self._duration:  # 时间用完就结束
                break
            event.run()                      # 模拟这个事件，其运行可能生成新事件
            
    def add_event(self, event):
        self._eventq.enqueue(event)
        
    def cur_time(self):
        return self._time

"""
公共事件基类
"""        
class Event:
    def __init__(self, event_time, host):
        self._ctime = event_time
        self._host = host         # 宿主系统
        
    def __lt__(self, other_event):
        return self._ctime < other_event._ctime
        
    def __le__(self, other_event):
        return self._ctime <= other_event._ctime
        
    def host(self):
        return self._host
        
    def time(self):
        return self._ctime
    
    def run(self):  # 具体事件完成定义此方法
        pass
