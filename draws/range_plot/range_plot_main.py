# -*- coding: utf-8 -*-
# Description: 热力图实验对比

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


if __name__ == '__main__':
    x_lst = []
    y_lst = []
    with open("data_range/draws.txt", "r") as f:  # 打开文件
        for line in f.readlines():
            tmp_lst = line.strip().split(',')
            x, y = tmp_lst[0], tmp_lst[1]
            x_lst.append(x)
            y_lst.append(y)
            # print(data)
    plt.plot(x_lst, y_lst)
    plt.xticks([])
    plt.yticks([])
    plt.show()

