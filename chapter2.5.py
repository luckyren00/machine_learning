import torch
x = torch.arange(4.0)
x.requires_grad_(True)
x.grad
y = 2 * torch.dot(x,x)
print(y)
y.backward()
print(x.grad == 4 * x)
#非标量变量的反向传播
x.grad.zero_()
y = x*x
y.sum().backward()
print(x.grad)
#分离计算
x.grad.zero_()
y = x * x
u = y.detach()
z = u * x
z.sum().backward()
print(x.grad == u)
x.grad.zero_()
y.sum().backward()
print(x.grad == 2 * x)

#Python控制流的梯度计算
def f(a):
    b = a * 2
    while b.norm() < 1000:
        b = b * 2
    if b.sum() > 0:
        c = b
    else:
        c = 100 * b
    return c

a = torch.randn(size=(), requires_grad=True)
d = f(a)
d.backward()
d.backward()
print(a.grad == d / a)

labels = torch.tensor([0,1,2])
num_classs = 3
#独热编码
onehot = torch.eye(num_classs)[labels]
print(onehot)
