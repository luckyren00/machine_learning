import os
import torch
import numpy
import pandas as pd

# os.makedirs(os.path.join(r'E:\python_project\machine_learning','data'), exist_ok=True)
data_file = os.path.join(r'E:\python_project\machine_learning','data','house_tiny.csv')
#
# with open(data_file, 'w') as f:
#     f.write('NumRooms, Alley, Price\n')
#     f.write('NA,Pave,127500\n')
#     f.write('2,NA,10600\n')
#     f.write('4,NA,178100\n')
#     f.write('NA,NA,140000\n')

data = pd.read_csv(data_file)
# print(type(data))
print(data)
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]

"""
原书中代码如下：inputs = inputs.fillna(inputs.mean()) 这样会报错TypeError: can only concatenate str (not "int") to str
应该是pandas版本问题造成的。
"""
inputs['NumRooms'] = inputs['NumRooms'].fillna(inputs['NumRooms'].mean())
print(inputs)
"""
原书中pd.get_dummies(inputs, dummy_na=True)的结果中Alley_Pave Alley_nan的值均为Ture或者False,而不是0和1
这时由于pandas版本导致的，在Pandas1.6.0之前热编码结果是0和1，但是1.6.0之后默认是bool值，但是可自己制定dtype类型
"""
# inputs = pd.get_dummies(inputs, dummy_na=True, dtype=numpy.int8)
# print(inputs)

# x = torch.tensor(inputs.to_numpy(dtype=float))
# y = torch.tensor(outputs.to_numpy(dtype=float))
# print("x = ",x)
# print("y = ",y)
number = inputs.count(axis=0)
print(number)
#练习题：删除NaN值最多的列
inputs = inputs.drop(inputs.count(axis=0).idxmin(),axis=1)
print(inputs)
x = torch.tensor(inputs.to_numpy(dtype=float))
print(x)


