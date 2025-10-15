import numpy as np
import matplotlib.pyplot as plt

"""
指数增长模型（Exponential Growth Model）
==========================================
模型公式：y = M * (1 - e^(-k*x)) + c

参数说明：
- M: 最大增长幅度（Maximum growth amplitude）
      控制从初始值到目标值的总变化量
      M = 目标值 - 初始值 = 1 - 0.001 = 0.999
      
- k: 增长速率（Growth rate）
      控制曲线增长的快慢
      k 越大，增长越快（曲线越陡峭）
      k 越小，增长越慢（曲线越平缓）
      
- c: 初始值（Initial value）
      曲线的起始点
      在本例中 c = 0.001
      
模型特点：
1. 单调递增，永不递减
2. 存在上渐近线（y → M + c）
3. 初期增长快，后期趋于平缓
4. 适合描述有上限的增长过程（如学习曲线、市场渗透率等）
"""

init_value = 0.001
max_value = 0.5
count = 4000

def exp_model(x, M, k):
    """
    指数增长函数
    
    参数:
        x: 自变量（可以是单个值或numpy数组）
        M: 最大增长幅度
        k: 增长速率
    
    返回:
        y: 函数值
    """
    return M * (1 - np.exp(-k * x)) + init_value

# ============= 生成数据点 =============
# 使用 np.arange 生成整数序列
# 参数说明：
#   - 起始值: 0（从0开始，确保第一个y值等于init_value）
#   - 终止值: count（不包含count，所以最后一个是count-1）
#   - 步长: 1（默认，每次递增1）
# 生成的序列：[0, 1, 2, 3, ..., count-1]，共count个点
x = np.arange(0, count)

# ============= 设置不同的参数组合 =============
# 每组参数展示不同的增长速率
params = [
    {'k': 0.0001, 'label': 'k=0.05 (Gentle)'},      # 温和增长：增长缓慢
    # {'k': 0.1, 'label': 'k=0.1 (Moderate)'},    # 适中增长：中等速度
    # {'k': 0.2, 'label': 'k=0.2 (Steep)'}        # 陡峭增长：增长快速
]

# ============= 绘制曲线 =============
# 坐标系说明：
#   x轴：点数（从0到2000）- 表示经过多少个采样点
#   y轴：函数值（从0.001到1）- 表示在该点处达到的值
plt.figure(figsize=(8, 6))

# 验证：第一个点（x=0）的y值应该等于init_value
print("第一个点 x=0 时，y =", exp_model(0, M=max_value-init_value, k=0.0001))

for param in params:
    # 计算每个x对应的y值
    y_values = exp_model(x, M=max_value-init_value, k=param['k'])
    
    # 生成点的索引序列：[0, 1, 2, ..., 1999]
    point_indices = np.arange(len(y_values))
    
    # for i in range(len(y_values)):
    #     if i % 50 == 0:
    #         print(point_indices[i], y_values[i])
    
    # 绘制曲线：横轴为点数，纵轴为函数值
    plt.plot(point_indices, y_values, label=param['label'])

# ============= 添加参考线和标注 =============
# 添加目标值水平线（y=1）
plt.axhline(y=max_value, color='r', linestyle='--', label='Target Value (y={})'.format(max_value))

# 添加初始值水平线（y=0.001）
plt.axhline(y=init_value, color='g', linestyle='--', label='Initial Value (y={})'.format(init_value))

# 标注起始点
plt.scatter([0], [init_value], color='red', zorder=5, label='Starting Point (0, {})'.format(init_value))

# ============= 设置图表属性 =============
plt.xlabel('Number of Points (0 to {})'.format(count))  # x轴标签：点数
plt.ylabel('Function Value ({} to {})'.format(init_value, max_value))   # y轴标签：函数值
plt.title('Exponential Growth Speed Comparison: Value at each point')  # 图表标题
plt.legend()      # 显示图例
plt.grid(True)    # 显示网格线
plt.show()        # 显示图表