import torch

# x = torch.tensor(3.0)
# y = torch.tensor(2.0)
#
# print("x + y = ", x + y)
# print("x * y = ", x * y)
# print("x / y = ", x / y)
# print("x ** y = ",x ** y)

x = torch.arange(4,dtype=torch.float32)
print("x = ", x)
print("x1 = ", x[1])

A = torch.arange(20).reshape(5,4)
print(A)
print(A.T)

B = torch.arange(24).reshape(2,3,4)
print("B:\n",B)

C = torch.arange(20, dtype=torch.float32).reshape(5,4)
D = C.clone()
print("C : \n", C)
print("C + D:\n", C+D)
print("C * D:", C*D)
print(C.sum(),C.sum(axis=0),C.sum(axis=1))
print(C.numel())
print(C.cumsum(axis=0))
print(C.sum(axis=1,keepdims=True))
"""
torch.dot()只能对一维张量进行点积运算，且不能广播
"""
# print(torch.dot(C,D))
print(torch.sum(C*D))

"""
矩阵和向量的乘积通过mv函数实现，要求：矩阵的列维数和向量的维数必须相同,数据类型也要一样
"""

print(C.shape)
print(x.shape)
print(torch.mv(C,x))

"""
矩阵-矩阵乘法：通过函数mm实现
"""
E = torch.ones(4,3)
print(E)
print(torch.mm(C,E))

"""
范数
"""
#L2范数
u = torch.tensor([3.0,-4.0])
print(torch.norm(u))
#L1范数:表示向量元素绝对值之和
print(torch.abs(u).sum())
#Frobenius范数
print(torch.norm(torch.ones(4,9)))

M = torch.arange(24,dtype=torch.float32).reshape(2,3,4)
print(len(M))
print(M.sum(axis=0))
print(M.sum(axis=1))
print(M.sum(axis=2))