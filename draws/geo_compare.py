# -*- coding: utf-8 -*-
# Description: 热力图实验对比

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    figure = plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.bar([9, 14, 19, 24, 29], [4, 14, 27, 58, 95])
    plt.bar([10, 15, 20, 25, 30], [1, 13, 22, 51, 86])
    plt.bar([11, 16, 21, 26, 31], [13, 34, 59, 82, 133])
    plt.xlabel("Data Size(%)")
    plt.ylabel("Insert Time(s)")
    plt.legend(["JUST", "Geomesa", "Mine"])

    # 画第4个图：条形图
    plt.subplot(122)
    plt.bar([19, 39, 59, 79, 99], [0.012, 0.056, 0.12, 0.21, 0.36])
    plt.bar([20, 40, 60, 80, 100], [0.01, 0.057, 0.11, 0.19, 0.34])
    plt.bar([21, 41, 61, 81, 101], [0.01, 0.055, 0.13, 0.25, 0.41])
    plt.xlabel("Data Size(%)")
    plt.ylabel("Query Time(s)")
    plt.legend(["JUST", "Geomesa", "Mine"])

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.show()
