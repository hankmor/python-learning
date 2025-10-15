import numpy as np
import matplotlib.pyplot as plt

"""
幂函数增长模型（Power Function Growth Model）
==========================================
模型公式：y = a * x^b + c

参数说明：
- a: 缩放系数（Scale coefficient）
      控制曲线的整体幅度
      a 越大，曲线整体越高
      决定增长的强度
      
- b: 幂指数（Power exponent）
      控制曲线的增长形状和速度
      b < 1: 递减增长率（前期快，后期慢）- 边际效应递减
      b = 1: 线性增长
      b > 1: 递增增长率（前期慢，后期快）- 加速增长
      
      在本例中：
      - b = 0.2: 非常陡峭，快速达到饱和
      - b = 0.5: 平方根型增长，适中
      - b = 0.8: 较平缓，持续增长
      
- c: 常数项（Constant term）
      曲线的最小值/起始值
      在本例中 c = 0.001
      
模型特点：
1. 单调递增（当 a>0, b>0 时）
2. 没有上渐近线（理论上可无限增长）
3. 当 b<1 时，增长率递减（适合描述学习效率、技能提升等）
4. 当 b>1 时，增长率递增（适合描述复利增长、指数爆发等）
5. 灵活性高，可通过调整 b 值模拟不同的增长模式
"""

def power_model(x, a, b):
    """
    幂函数增长模型
    
    参数:
        x: 自变量（可以是单个值或numpy数组）
        a: 缩放系数
        b: 幂指数
    
    返回:
        y: 函数值
    """
    return a * x**b + 0.001

# ============= 生成数据点 =============
# 使用 np.linspace 生成等间距的 x 值
# 参数说明：
#   - 起始值: 0.0001（避免 x=0 时某些幂运算未定义）
#   - 终止值: 1
#   - 点数: 2000（生成2000个等间距的点）
# 注意：x 的范围较小（0.0001到1），这样可以观察到幂函数在小数范围内的行为
x = np.linspace(0.0001, 1, 2000)

# ============= 设置不同的参数组合 =============
# 每组参数展示不同的幂指数效果
# a 值经过精心调整，使得不同 b 值的曲线都能从 0.001 增长到接近 1
params = [
    {'b': 0.2, 'a': 0.3977, 'label': 'b=0.2 (Steep)'},      # 陡峭型：快速增长后趋于平缓
    {'b': 0.5, 'a': 0.0999, 'label': 'b=0.5 (Moderate)'},   # 适中型：平方根增长
    {'b': 0.8, 'a': 0.0251, 'label': 'b=0.8 (Gentle)'}      # 平缓型：持续稳定增长
]

# ============= 绘制曲线 =============
# 坐标系说明：
#   x轴：点数（从0到2000）- 表示经过多少个采样点
#   y轴：函数值（从0.001到1）- 表示在该点处达到的值
plt.figure(figsize=(8, 6))

for param in params:
    # 计算每个x对应的y值
    y_values = power_model(x, param['a'], param['b'])
    
    # 生成点的索引序列：[0, 1, 2, ..., 1999]
    point_indices = np.arange(len(y_values))
    
    # 绘制曲线：横轴为点数，纵轴为函数值
    plt.plot(point_indices, y_values, label=param['label'])

# ============= 添加参考线和标注 =============
# 添加目标值水平线（y=1）
plt.axhline(y=1, color='r', linestyle='--', label='Target Value (y=1)')

# 添加初始值水平线（y=0.001）
plt.axhline(y=0.001, color='g', linestyle='--', label='Initial Value (y=0.001)')

# ============= 设置图表属性 =============
plt.xlabel('Number of Points (0 to 2000)')  # x轴标签：点数
plt.ylabel('Function Value (0.001 to 1)')   # y轴标签：函数值
plt.title('Power Function Growth Speed Comparison: Value at each point')  # 图表标题
plt.legend()      # 显示图例
plt.grid(True)    # 显示网格线
plt.show()        # 显示图表