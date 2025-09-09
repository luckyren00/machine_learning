import torch
from torch.utils.tensorboard import SummaryWriter

#确保cuda可用
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#生成数据
inputs = torch.rand(100,3)
weights = torch.tensor([[1.1],[2.2],[3.3]])
bias = torch.tensor(4.4)

targets = inputs @ weights + bias + 0.1 * torch.randn(100,1)

#创建一个SummaryWriter实例
writer = SummaryWriter(log_dir = "E:/python_project/machine_learning/run/")
#初始化参数时直接放到cuda上
w = torch.rand((3,1), requires_grad = True, device = device)
b = torch.rand((1,), requires_grad = True, device = device)

#进行训练
inputs = inputs.to(device)
targets = inputs.to(device)

#设置超参数
epoch = 10000
lr = 0.003

for i in range(epoch):
    outputs = inputs @ w + b
    loss = torch.mean((torch.square(outputs - targets)))
    print("loss:", loss.item()) #item()将单元素张量转化为python原生浮点数
    #记录loss,三个参数分别：tag,loss值，第几步
    writer.add_scalar("loss/train", loss.item(), i)
    loss.backward()
    #下面的计算不需要梯度跟踪
    with torch.no_grad():
        w -=lr * w.grad
        b -=lr * b.grad

    #梯度清零
    w.grad.zero_()
    b.grad.zero_()

print("训练后的权重 w:", w)
print("训练后的偏置 b:", b)