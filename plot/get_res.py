import os
# 绘图
import matplotlib.pyplot as plt
import numpy as np

with open("log.txt") as f:
    lines = f.readlines()
    name = None
    acc = None
    acc_list = []
    for line in lines:
        if "test_acc1" in line:
            acc = float(line[line.index("test_acc1")+12+1:line.index(', "test_acc5":')])
            acc_list.append(acc*100)
        else:
            if name is not None and acc is not None:
                print(name, acc)
            name = line[:-1]
# 绘制acc曲线
x = np.arange(0, len(acc_list))
plt.plot(x, acc_list, label="acc", marker='o')
plt.xlabel("remove layer")
plt.ylabel("acc")
# 画一条横线：baseline
plt.axhline(y=72.2, color='r', linestyle='--', label="baseline")
# 设置y轴范围
plt.ylim(0, 100)
plt.legend()
plt.savefig("remove_acc_tiny.png")