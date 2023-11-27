"""
使用 greeting 模块
"""

import greeting.greeting as gs


# gs 为模块别名，通过 gs 调用方法
gs.greeting("lisi")
# python没有强制禁止调用私有成员的机制
gs._sayHello("lisi")
