import torch

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.tensor(1.0, dtype = torch.float32, requires_grad=True, device='cuda')
# x_cpu = torch.tensor(1.0, dtype = torch.float32, requires_grad=True)
y = torch.tensor(1.0, dtype = torch.float32, requires_grad=True, device='cuda')
# x = x_cpu.to(device)
# y = y_cpu.to(device)
v = 3 * x + 4 * y
u = torch.square(v)
z = torch.log(u)

z.backward() #反向传播求梯度

print("x grad:", x.grad)
print("y grad:", y.grad)

