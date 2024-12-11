import os
# 绘图
import matplotlib.pyplot as plt
import numpy as np

with open("log_small.txt") as f:
    lines = f.readlines()
    name = None
    acc = None
    acc_small_list = []
    for line in lines:
        if "test_acc1" in line:
            acc = float(line[line.index("test_acc1")+12+1:line.index(', "test_acc5":')])
            acc_small_list.append(acc)
        else:
            if name is not None and acc is not None:
                print(name, acc)
            name = line[:-1]
            
with open("log_tiny.txt") as f:
    lines = f.readlines()
    name = None
    acc = None
    acc_tiny_list = []
    for line in lines:
        if "test_acc1" in line:
            acc = float(line[line.index("test_acc1")+12+1:line.index(', "test_acc5":')])
            acc_tiny_list.append(acc)
        else:
            if name is not None and acc is not None:
                print(name, acc)
            name = line[:-1]
# 绘制acc曲线
x = np.arange(0, len(acc_small_list))
plt.plot(x, acc_small_list, label="deit_small", marker='o')
plt.plot(x, acc_tiny_list, label="deit_tiny", marker='o')
plt.xlabel("remove layer")
plt.ylabel("acc")
# 画一条横线：baseline
plt.axhline(y=79.9, color='r', linestyle='--', label="baseline_small")
plt.axhline(y=72.2, color='g', linestyle='--', label="baseline_tiny")
# 设置y轴范围
plt.ylim(0, 100)
# 设置title
plt.title("acc with remove layer in deit small and tiny")
plt.legend()
plt.savefig("remove_acc.png")