import numpy as np
import matplotlib.pyplot as plt

"""
指数增长模型（前期快，后期慢）- 支持反函数计算
==========================================
模型公式：y = M * (1 - e^(-k*x)) + c

其中：
- M: 最大增长幅度 (max_value - init_value)
- k: 增长速率（控制增长快慢）
- c: 初始值

模型特点：
1. 前期增长快，后期趋缓（递减增长率）
2. 有上渐近线 y → M + c
3. 支持反函数：给定 y 值，可以计算 x 值

反函数公式：x = -ln(1 - (y - c) / M) / k
"""

# ============= 参数设置 =============
init_value = 500        # y轴初始值（当x=1时）
max_value = 5000000     # y轴最大值（渐近线）
min_x = 1               # x轴起始值
max_x = 160             # x轴最大值

# 计算模型参数
M = max_value - init_value  # 最大增长幅度
c = init_value              # 初始值常数项

# 计算k值：确保当x=1时，y=init_value
# init_value = M * (1 - e^(-k*1)) + c
# 0 = M * (1 - e^(-k))
# e^(-k) = 1
# 这要求 k → 0，但这样曲线太平缓

# 更好的方法：使用第二个约束点来确定k
# 假设当 x=max_x/2=80 时，y 应该达到某个中间值
# 或者设置一个合理的k值，让曲线在x=max_x时接近max_value

# 方案1：设定k值，让曲线在x=max_x时达到max_value的95%
target_ratio = 0.95  # 在x=max_x时达到95%的最大值
# target_ratio = (y - c) / M = 1 - e^(-k*max_x)
# e^(-k*max_x) = 1 - target_ratio
# k = -ln(1 - target_ratio) / max_x
k = -np.log(1 - target_ratio) / max_x

print("=" * 70)
print("指数增长模型参数：")
print(f"  x 范围: {min_x} 到 {max_x}")
print(f"  y 范围: {init_value:,} 到 {max_value:,}")
print(f"  M (增长幅度) = {M:,}")
print(f"  k (增长速率) = {k:.6f}")
print(f"  c (初始常数) = {c}")
print("=" * 70)


# ============= 定义函数 =============
def exp_forward(x, M, k, c):
    """
    正向函数：根据 x 计算 y
    
    参数:
        x: x值（可以是单个值或numpy数组）
        M: 最大增长幅度
        k: 增长速率
        c: 初始值常数
    
    返回:
        y: 对应的y值
    """
    return M * (1 - np.exp(-k * x)) + c


def exp_inverse(y, M, k, c):
    """
    反函数：根据 y 计算 x
    
    参数:
        y: y值（可以是单个值或numpy数组）
        M: 最大增长幅度
        k: 增长速率
        c: 初始值常数
    
    返回:
        x: 对应的x值
    
    推导过程：
        y = M * (1 - e^(-k*x)) + c
        y - c = M * (1 - e^(-k*x))
        (y - c) / M = 1 - e^(-k*x)
        e^(-k*x) = 1 - (y - c) / M
        -k*x = ln(1 - (y - c) / M)
        x = -ln(1 - (y - c) / M) / k
    """
    ratio = (y - c) / M
    
    # 确保 ratio 在有效范围内 (0, 1)
    if isinstance(ratio, np.ndarray):
        ratio = np.clip(ratio, 1e-10, 0.9999)
    else:
        ratio = max(1e-10, min(ratio, 0.9999))
    
    x = -np.log(1 - ratio) / k
    return x


# ============= 生成数据点 =============
x = np.arange(min_x, max_x + 1)  # [1, 2, 3, ..., 160]
y = exp_forward(x, M, k, c)

# ============= 验证反函数 =============
print("\n" + "=" * 70)
print("验证反函数功能：")
print("=" * 70)

# 测试几个y值
test_y_values = [500, 50000, 500000, 1000000, 2500000, 4000000]

print("\n给定 y 值，计算对应的 x 值：")
print(f"{'y 值':<15} {'计算得到的 x':<15} {'验证：y=f(x)':<20} {'误差'}")
print("-" * 70)

for test_y in test_y_values:
    if test_y <= max_value:
        calc_x = exp_inverse(test_y, M, k, c)
        verify_y = exp_forward(calc_x, M, k, c)
        error = abs(verify_y - test_y)
        print(f"{test_y:<15,} {calc_x:<15.2f} {verify_y:<20,.2f} {error:.2e}")

# ============= 关键点验证 =============
print("\n" + "=" * 70)
print("关键点验证：")
print("=" * 70)

y_at_1 = exp_forward(1, M, k, c)
y_at_80 = exp_forward(80, M, k, c)
y_at_160 = exp_forward(160, M, k, c)

print(f"  x=1:   y = {y_at_1:,.2f}")
print(f"  x=80:  y = {y_at_80:,.2f} ({y_at_80/max_value*100:.1f}% of max)")
print(f"  x=160: y = {y_at_160:,.2f} ({y_at_160/max_value*100:.1f}% of max)")

print("\n反向验证：")
x_at_500 = exp_inverse(500, M, k, c)
x_at_2500000 = exp_inverse(2500000, M, k, c)
print(f"  y=500:       x = {x_at_500:.2f}")
print(f"  y=2,500,000: x = {x_at_2500000:.2f}")

print("=" * 70)


# ============= 绘制曲线 =============
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 左图：正向函数 (x → y)
ax1.plot(x, y, linewidth=2.5, color='blue', label='y = f(x)')
ax1.scatter([1], [y_at_1], color='green', s=150, zorder=5, marker='o', 
            edgecolors='black', linewidths=2, label=f'Start: (1, {y_at_1:,.0f})')
ax1.axhline(y=max_value, color='r', linestyle='--', linewidth=1, alpha=0.7, 
            label=f'Asymptote: y={max_value:,}')
ax1.set_xlabel('x (1 to 160)', fontsize=12)
ax1.set_ylabel('y (500 to 5,000,000)', fontsize=12)
ax1.set_title('Forward Function: y = f(x)', fontsize=13, fontweight='bold')
ax1.legend(loc='lower right', fontsize=10)
ax1.grid(True, alpha=0.3, linestyle='--')

# 右图：反函数 (y → x)
y_range = np.linspace(500, max_value * 0.99, 1000)
x_from_y = exp_inverse(y_range, M, k, c)

ax2.plot(y_range, x_from_y, linewidth=2.5, color='red', label='x = f⁻¹(y)')
ax2.scatter([y_at_1], [1], color='green', s=150, zorder=5, marker='o',
            edgecolors='black', linewidths=2, label=f'Start: ({y_at_1:,.0f}, 1)')

# 标注几个示例点
for test_y in [500000, 2000000, 4000000]:
    test_x = exp_inverse(test_y, M, k, c)
    ax2.scatter([test_y], [test_x], s=100, zorder=4, alpha=0.7)
    ax2.annotate(f'({test_y/1000:.0f}k, {test_x:.1f})', 
                xy=(test_y, test_x), xytext=(10, -20),
                textcoords='offset points', fontsize=9,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

ax2.set_xlabel('y (500 to 5,000,000)', fontsize=12)
ax2.set_ylabel('x (1 to 160)', fontsize=12)
ax2.set_title('Inverse Function: x = f⁻¹(y)', fontsize=13, fontweight='bold')
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('exponential_growth_with_inverse.png', dpi=150, bbox_inches='tight')
print("\n图表已保存为: exponential_growth_with_inverse.png")
plt.show()


# ============= 使用示例 =============
print("\n" + "=" * 70)
print("使用示例代码：")
print("=" * 70)
print("""
# 1. 根据 x 计算 y
x_value = 50
y_value = exp_forward(x_value, M, k, c)
print(f"当 x={x_value} 时，y={y_value:,.2f}")

# 2. 根据 y 计算 x（关键功能！）
y_target = 1000000
x_needed = exp_inverse(y_target, M, k, c)
print(f"要达到 y={y_target:,}，需要 x={x_needed:.2f}")

# 3. 批量计算
y_targets = [1000, 10000, 100000, 1000000]
x_results = [exp_inverse(y, M, k, c) for y in y_targets]
for y, x in zip(y_targets, x_results):
    print(f"  y={y:>10,} → x={x:>6.2f}")
""")
print("=" * 70)
