# encoding:utf-8

"""
实现海关检查站模拟系统
"""
from random import randint
from SQueue import SQueue
from simulation import Simulation, Event

"""
实际的模拟类
"""
class Customs:
    def __init__(self, gate_num, duration, arrive_interval, check_interval):
        self.simulation = Simulation(duration)
        self.waitline = SQueue()                # 等待队列
        self.duration = duration
        self.gates = [0]*gate_num               # 通道列表，0表示空闲
        self.total_wait_time = 0
        self.total_used_time = 0
        self.car_num = 0
        self.arrive_interval = arrive_interval  # 到达时间的间隔
        self.check_interval = check_interval    # 检查时间的范围
        
    def wait_time_acc(self, n):
        self.total_wait_time += n
        
    def total_time_acc(self, n):
        self.total_used_time += n
        
    def car_count_1(self):
        self.car_num += 1
        
    def add_event(self, event):
        self.simulation.add_event(event)
        
    def cur_time(self):
        return self.simulation.cur_time()
        
    def enqueue(self, car):
        self.waitline.enqueue(car)
        
    def has_queued_car(self):
        return not self.waitline.is_empty()
        
    def next_car(self):
        return self.waitline.dequeue()
        
    def find_gate(self):
        for i in range(len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None
        
    def free_gate(self, i):
        if self.gates[i] == 1:
            self.gates[i] = 0
        else:
            raise ValueError("free gate error")
    
    # 实施模拟        
    def simulate(self):
       Arrive(0, self)  # 汽车到达事件，初始化生成一辆车
       self.simulation.run()
       self.statistics()
       
    # 输出统计数据
    def statistics(self):
        print("Simulation " + str(self.duration) + " minutes, for " + str(len(self.gates)) + " gates")
        print(self.car_num, " cars pass the customs")
        print("Average waiting time: ", self.total_wait_time/self.car_num)
        print("Average passing time: ", self.total_used_time/self.car_num)
        i = 0
        while not self.waitline.is_empty():
            self.waitline.dequeue()
            i += 1
        print(i, " cars are in waiting line")
        
"""
汽车类
"""
class Car:
    def __init__(self, arrive_time):
        self.time = arrive_time  # 到达时间
        
    def arrive_time(self):
        return self.time

# 日志输出        
def event_log(time, name):
    print("Event: " + name + ", happens at " + str(time))
    
"""
事件类
"""
# 汽车到达事件
class Arrive(Event):
    def __init__(self, arrive_time, customs):
        super().__init__(arrive_time, customs)
        customs.add_event(self)  # 加入到事件队列中
    
    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, "car arrive")
        # 生成下一个Arrive事件
        Arrive(time + randint(*customs.arrive_interval), customs)
        # 该车辆执行
        car = Car(time)
        if customs.has_queued_car():  # 前面有其他车辆在等,进入等待队列
            customs.enqueue(car)
            return
        i = customs.find_gate()  # 检查空闲通道
        if i is not None:
            event_log(time, "car check")
            Leave(time + randint(*customs.check_interval), i, car, customs)
        else:
            customs.enqueue(car)

# 汽车离开事件 
class Leave(Event):
    def __init__(self, leave_time, gate_num, car, customs):
        super().__init__(leave_time, customs)
        self.car = car
        self.gate_num = gate_num
        customs.add_event(self)
        
    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, "car leave")
        customs.free_gate(self.gate_num)
        customs.car_count_1()
        customs.total_time_acc(time - self.car.arrive_time())
        if customs.has_queued_car():
            car = customs.next_car()
            customs.find_gate()
            event_log(time, "car check")
            customs.wait_time_acc(time - car.arrive_time())
            Leave(time + randint(*customs.check_interval), self.gate_num, car, customs)

if __name__ == '__main__':
    car_arrive_interval = (1, 2)
    car_check_time = (3, 5)
    cus = Customs(3, 120, car_arrive_interval, car_check_time)
    cus.simulate()
