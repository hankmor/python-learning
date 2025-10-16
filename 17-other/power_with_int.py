import numpy as np
import matplotlib.pyplot as plt

"""
幂函数加速增长模型（Power Function Accelerating Growth Model）
==========================================
模型公式：y = a * x^b + c 

其中：
- b > 1：实现前期慢后期快的加速增长
- c：常数项（自动计算，确保当 x=1 时，y=init_value）

本文件展示 b > 1 的情况，曲线特点：
- 从点 (1, init_value) 开始，如 (1, 100)
- 到点 (max_x, max_value) 结束，如 (145, 5000000)
- 前期增长缓慢，后期增长陡峭（加速增长）
- 类似于复利增长、网络效应等加速现象

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
      
      在本例中（加速增长，前期慢后期快）：
      - b = 1.2: 轻微加速增长
      - b = 1.5: 适中加速增长
      - b = 2.0: 二次方增长（平方）
      - b = 3.0: 三次方增长（立方）
      
- c: 常数项（Constant term）
      根据约束条件自动计算
      约束：当 x=1 时，y = init_value（如 100）
      公式：c = init_value - a
      
模型特点：
1. 单调递增（当 a>0, b>0 时）
2. 没有上渐近线（理论上可无限增长）
3. 当 b<1 时，增长率递减（适合描述学习效率、技能提升等）
4. 当 b>1 时，增长率递增（适合描述复利增长、指数爆发等）
5. 灵活性高，可通过调整 b 值模拟不同的增长模式
"""

def power_model(x, a, b, c):
    """
    幂函数增长模型
    
    参数:
        x: 自变量（可以是单个值或numpy数组）
        a: 缩放系数
        b: 幂指数
        c: 常数项（初始值）
    
    返回:
        y: 函数值 = a * x^b + c
    """
    return a * x**b + c

# ============= 生成数据点 =============
# 使用 np.arange 生成整数序列
# 参数说明：
#   - 起始值: 1（从1开始，因为当x=1时y=100）
#   - 终止值: 146（不包含，所以最后一个是145）
#   - 步长: 1（默认，每次递增1）
# 生成的序列：[1, 2, 3, ..., 144, 145]，共145个点
x = np.arange(1, 146)

# ============= 设置目标参数 =============
init_value =  100         # y轴初始值
max_value = 5000000     # y轴最大值
max_x = 145             # x轴最大值

# ============= 设置不同的参数组合 =============
# 每组参数展示不同的幂指数效果（b > 1：前期慢，后期快）
# 计算 a 和 c 值：
# 公式：y = a * x^b + c
# 约束条件：
#   当 x=1 时：y=init_value → 100 = a * 1^b + c = a + c
#   当 x=max_x 时：y=max_value → 5000000 = a * max_x^b + c
# 解方程：
#   从第一个等式：c = init_value - a
#   代入第二个：max_value = a * max_x^b + (init_value - a)
#              max_value = a * (max_x^b - 1) + init_value
#              a = (max_value - init_value) / (max_x^b - 1)
#              c = init_value - a

params = []
for b_val in [1.5, 2.0, 2.5, 3.0]:
    a_val = (max_value - init_value) / (max_x ** b_val - 1)
    c_val = init_value - a_val
    print(f"b: {b_val}, a: {a_val}, c: {c_val}")
    label_map = {1.5: 'Moderate acceleration', 2.0: 'Quadratic', 2.5: 'Strong acceleration', 3.0: 'Cubic'}
    params.append({'b': b_val, 'a': a_val, 'c': c_val, 'label': f'b={b_val} ({label_map[b_val]})'})


# ============= 绘制曲线 =============
# 坐标系说明：
#   x轴：从1到145 - 表示x值
#   y轴：从100到5000000 - 表示在该x值处的y值
plt.figure(figsize=(10, 6))

print("=" * 70)
print(f"加速增长模型参数验证（b > 1：前期慢，后期快）")
print(f"x轴范围：1 到 {max_x}")
print(f"y轴范围：{init_value} 到 {max_value:,}")
print("=" * 70)

for param in params:
    # 计算每个x对应的y值（使用各自计算的常数项 c）
    y_values = power_model(x, param['a'], param['b'], param['c'])
    
    # 验证关键点的值
    y_start = y_values[0]  # 第一个点（x=1）
    y_mid = y_values[len(y_values)//2]  # 中间点（x≈73）
    y_end = y_values[-1]  # 最后一个点（x=145）
    
    print(f"\n{param['label']}:")
    print(f"  起始点 (x=1):      y = {y_start:,.0f} (应为 {init_value})")
    print(f"  中间点 (x≈73):     y ≈ {y_mid:,.0f}")
    print(f"  终止点 (x={max_x}):    y = {y_end:,.0f} (应为 {max_value:,})")
    print(f"  参数 a = {param['a']:.6f}, b = {param['b']}, c = {param['c']:.6f}")
    
    # 绘制曲线：横轴为x值，纵轴为y值
    plt.plot(x, y_values, label=param['label'], linewidth=2)

print("=" * 70)

# ============= 添加参考线和标注 =============
# 添加最大值水平线
plt.axhline(y=max_value, color='r', linestyle='--', linewidth=1, alpha=0.7, 
            label=f'Max Value (y={max_value:,})')

# 添加初始值水平线
plt.axhline(y=init_value, color='g', linestyle='--', linewidth=1, alpha=0.7, 
            label=f'Initial Value (y={init_value})')

# 标注起始点（x=1, y=init_value）
plt.scatter([1], [init_value], color='green', s=100, zorder=5, marker='o', 
            label=f'Start Point (1, {init_value})')

# 标注终止点（x=max_x, y=max_value）
plt.scatter([max_x], [max_value], color='red', s=100, zorder=5, marker='o',
            label=f'End Point ({max_x}, {max_value:,})')

# ============= 设置图表属性 =============
plt.xlabel(f'x (1 to {max_x})', fontsize=12)  # x轴标签
plt.ylabel(f'y ({init_value} to {max_value:,})', fontsize=12)  # y轴标签
plt.title('Power Function Accelerating Growth (b>1): Slow Start, Fast Finish', fontsize=14)  # 图表标题
plt.legend(loc='upper left', fontsize=9)  # 显示图例
plt.grid(True, alpha=0.3)    # 显示网格线
plt.tight_layout()           # 自动调整布局
plt.show()                   # 显示图表