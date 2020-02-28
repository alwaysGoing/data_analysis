import numpy as np

# 创建数组
# 从序列型对象创建

a = [1, 2, 3]
b = (1, 2, 3)

arr_1 = np.array(a)
print("从列表创建")
print(arr_1)
print("从元组创建")
arr_2 = np.array(b)
print(arr_2)

# 查看数组的维度（ndim）和形状（shape）
c = [[1, 2, 3], [4, 5, 6]]
arr_3 = np.array(c)
print("数组的dim：", arr_3.ndim)
print("数组的shape：", arr_3.shape)

# 查看数组类型
print("数组的类型：", arr_3.dtype)
print('--------------------------------------------')

# 创建全0数组
a = np.zeros([2, 3])
print("全0数组：")
print(a)

# 创建全1数组
a = np.ones([1, 2])
print("全1数组：")
print(a)

# 创建空数组，与全0数组不同
a = np.empty([2, 3])
print("空数组：")
print(a)
print('--------------------------------------------')

# arange函数，在numpy里是生成器的方式实现的
a = np.arange(10)
print("arange函数：", a)
print(a.dtype)
print('--------------------------------------------')

# zeros_like，ones_like，empty_like函数以数组作为输入，输出的数组的形状对应于输入的数组的形状
a = np.zeros_like(a)
print("zeros_like函数：", a)

# as_type函数可以改变数组的数值类型
print("a原来的类型：", a.dtype)
b = a.astype(np.float64)
print(a.dtype)
print("b的类型", b.dtype)
print('--------------------------------------------')

# numpy中的+，-，*，/都是逐元素进行的
a = np.zeros([2, 3])
b = np.ones([2, 3])
print("a-b=")
c = a - b
print(c)

# 有两种方式获取数组中的某个元素
print(c[0, 0])
print(c[0][0])
print("两种方式是等价的")
print('-------------------------------------------')

# 布尔型索引
a = np.array([1, 2, 3, 3, 4, 5, 5, 5])
print("获取数组中等于3的元素")
print(a == 3)
print(a[a == 3])
print('-------------------------------------------')

# reshape方法
print('reshape方法')
a = np.arange(10)
a = a.reshape([2, 5])
print(a)
print('-------------------------------------------')

# 转置
a = np.arange(16).reshape([2, 2, 4])
print("转置之前")
print(a)
b = a.transpose([1, 0, 2])
print(b)
print('-------------------------------------------')

# 开方
a = np.arange(10)
c = np.arange(1, 11)
print("开方后")
print(np.sqrt(a))
print("最大值：", np.max(a))
print("最小值：", np.min(a))
print("测试maximum和minimum")
print(np.maximum(a, c))
print(np.minimum(a, c))
print('-------------------------------------------')

# 测试modf，返回整数和小数部分
a = np.random.randn(5) * 10
print(a)
b = np.modf(a)
print(b)

# 测试meshgrid函数
print("测试meshgrid函数")
a = np.arange(5)
xs, ys = np.meshgrid(a, a)
print("xs")
print(xs)
print("ys")
print(ys)
print('----------------------------------------------')

# 条件逻辑表示为数组
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)
print("使用where")
result = np.where(cond, xarr, yarr)
print(result)

a = np.where(xarr > 1.3, 0, 1)
print(a)
print(xarr)
a = np.where(xarr>1.3, 0, xarr)
print(a)
print('----------------------------------------------')


