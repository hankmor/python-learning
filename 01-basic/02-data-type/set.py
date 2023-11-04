# set和dict类似。由于key不能重复，所以，在set中，没有重复的key。

# 从list创建set
s = set([1, 2, 3, "z", "a", 1, 2, 3])
print(s)  # {1, 2, 3, 'z', 'a'}

# 添加元素用add方法
s.add("A")
print(s)  # {1, 2, 3, 'A', 'z', 'a'}

# 移除元素用remove方法
s.remove(1)
print(s)  # {2, 3, 'z', 'A', 'a'}

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(s1 & s2)  # {3}，求交集
print(s1 | s2)  # {1, 2, 3, 4, 5}，求并集
print(s1 - s2)  # {1, 2}，求差集
print(s1 ^ s2)  # {1, 2, 4, 5}，求补集
