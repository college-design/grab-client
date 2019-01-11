#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import os
import sched

import grab.schedule.grab_job as grab_job

# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)

# 被周期性调度触发的函数
def execute_command(cmd, inc):
    print('执行主程序')
    ''''' 
    终端上显示当前计算机的连接情况 
    '''
    os.system(cmd)
    schedule.enter(inc, 0, execute_command, (cmd, inc))

def grab_data(cmd, inc):
    print(cmd)
    grab_job.batch_job1()
    schedule.enter(inc, 0, grab_data, (cmd, inc))

# type 调用的函数
def execute_main(type,cmd, inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    schedule.enter(0, 0, type, (cmd, inc))
    schedule.run()

# 每60秒查看下网络连接情况
if __name__ == '__main__':
    execute_main(execute_command,"netstat -an", 60)