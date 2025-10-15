import numpy as np
import matplotlib.pyplot as plt

"""
逻辑斯谛增长模型（Logistic Growth Model）
==========================================
模型公式：y = L / (1 + e^(-k*x)) + c

参数说明：
- L: 增长幅度（Growth amplitude）
      控制曲线上下渐近线之间的距离
      L = 上渐近线 - 下渐近线
      在本例中 L = 1
      
- k: 增长速率（Growth rate）
      控制曲线在拐点处的陡峭程度
      k 越大，增长越快（S型曲线越陡）
      k 越小，增长越慢（S型曲线越平缓）
      在本例中 k = 0.5
      
- c: 垂直偏移量（Vertical offset）
      控制曲线的整体上下位置
      决定下渐近线的位置
      在本例中 c = 0
      
模型特点：
1. S型曲线（Sigmoid curve）
2. 存在上下渐近线：下渐近线 y → c，上渐近线 y → L + c
3. 初期增长慢，中期加速，后期趋缓
4. 存在拐点：x=0 时 y=L/2+c（本例中为 y=0.5）
5. 适合描述有限资源下的增长过程（如人口增长、疫情传播等）
"""

def logistic(x, L=1, k=0.5, c=0):
    """
    逻辑斯谛增长函数
    
    参数:
        x: 自变量（可以是单个值或numpy数组）
        L: 增长幅度（默认为1）
        k: 增长速率（默认为0.5）
        c: 垂直偏移量（默认为0）
    
    返回:
        y: 函数值
    """
    return L / (1 + np.exp(-k * x)) + c

# ============= 生成数据点 =============
# 计算起始点：
# 当 y=0.001 时，求解 x 值：
# 0.001 = 1/(1 + e^(-0.5*x))
# 1 + e^(-0.5*x) = 1/0.001 = 1000
# e^(-0.5*x) = 999
# -0.5*x = ln(999)
# x = -ln(999)/0.5 ≈ -13.81

# 使用 np.linspace 生成等间距的 x 值
# 参数说明：
#   - 起始值: -13.81（对应 y≈0.001）
#   - 终止值: 10（对应 y≈0.999）
#   - 点数: 2000（生成2000个等间距的点）
x = np.linspace(-13.81, 10, 2000)
y = logistic(x)  # 计算对应的y值

# ============= 绘制曲线 =============
# 坐标系说明：
#   x轴：点数（从0到2000）- 表示经过多少个采样点
#   y轴：函数值（从0.001到1）- 表示在该点处达到的值
plt.figure(figsize=(8, 6))

# 生成点的索引序列：[0, 1, 2, ..., 1999]
point_indices = np.arange(len(y))

# 绘制曲线：横轴为点数，纵轴为函数值
plt.plot(point_indices, y, label='y = 1/(1 + e^(-0.5x))', color='blue')
# ============= 添加参考线和标注 =============
# 添加目标值水平线（y=1，上渐近线）
plt.axhline(y=1, color='r', linestyle='--', label='Target Value (y=1)')

# 添加初始值水平线（y=0.001）
plt.axhline(y=0.001, color='g', linestyle='--', label='Initial Value (y=0.001)')

# 添加拐点水平线（y=0.5，增长速度最快的点）
plt.axhline(y=0.5, color='orange', linestyle=':', label='Inflection Point (y=0.5)')

# 标注起始点
plt.scatter([0], [0.001], color='red', zorder=5, label='Starting Point (0, 0.001)')

# ============= 设置图表属性 =============
plt.xlabel('Number of Points (0 to 2000)')  # x轴标签：点数
plt.ylabel('Function Value (0.001 to 1)')   # y轴标签：函数值
plt.title('Logistic Growth Speed Comparison: Value at each point')  # 图表标题
plt.legend()      # 显示图例
plt.grid(True)    # 显示网格线
plt.show()        # 显示图表