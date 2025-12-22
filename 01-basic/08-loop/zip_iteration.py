# zip()：并行遍历

names = ["张三", "李四", "王五"]
ages = [25, 30, 35]
cities = ["北京", "上海", "广州"]

# zip打包成元组
for name, age, city in zip(names, ages, cities):
    print(f"{name}，{age}岁，来自{city}")

# 输出：
# 张三，25岁，来自北京
# 李四，30岁，来自上海
# 王五，35岁，来自广州
