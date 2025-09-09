import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("device name : ",device)
inputs = torch.tensor([[2,1000],[3,2000],[2,500],[1,800],[4,3000]],dtype=torch.float, device=device)
labels = torch.tensor([[19],[31],[14],[15],[43]], dtype = torch.float, device=device)

# #对输入数据进行归一化
# inputs = inputs / torch.tensor([4,3000], device=device)

#计算特征的均值和标准差
mean = inputs.mean(dim=0)
std = inputs.std(dim=0)
#对特征进行标准化
inputs_norm = (inputs - mean) /std


w = torch.ones(2,1, requires_grad=True, device=device)
b = torch.ones(1, requires_grad=True, device=device)

#epoch = 20
epoch = 1000
lr = 0.5
#lr = 0.0000001

for i in range(epoch):
    outputs = inputs_norm @ w + b
    loss = torch.mean(torch.square(outputs - labels))
    print("loss", loss.item())
    loss.backward()
    print("w.grad", w.grad.tolist())
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

    w.grad.zero_()
    b.grad.zero_()

#对新采集的数据进行预测
new_input = torch.tensor([[3,2500]], dtype=torch.float, device=device)
#对新的数据进行预测时，同样要进行标准化
new_input_norm = (new_input - mean) / std
#预测
predict = new_input_norm @ w + b
#打印预测结果
print("Predict:", predict.tolist()[0][0])