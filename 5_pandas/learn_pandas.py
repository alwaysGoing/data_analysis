import pandas as pd
from pandas import DataFrame, Series
import numpy as np

# 使用Series
a = Series([4, 7, -5, 3])
print(a)  # 由一组数据及与之对应的标签（即索引）构成，索引在左边，数值在右边
print("a的value：", a.values)
print("a的index：", a.index)
print("修改index和value")
a = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(a)
print('------------------------')

# 也可以使用索引
print(a['d'])
print(a[['d', 'a']])

# 也可以使用逻辑索引
print(a[a > 0])
print('--------------------------------------------------')

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj[:2])  # 不包含右边
print(obj['a':'c'])  # 包含右边
print('-----------------------------------------------')

# 测试DataFrame
print('测试DataFrame')
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
print(data, '\n\n\n')
print(data['three'] > 5, '\n\n\n')
print(data[data['three'] > 5], '\n\n\n')
print(data < 5, '\n\n\n')
