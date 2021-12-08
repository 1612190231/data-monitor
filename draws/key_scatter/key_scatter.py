# -*- coding: utf-8 -*-
# Description: 降维索引后的数据分布
# Created: luck 2021/11/30
from utils import csv_util
import matplotlib.pyplot as plt


if __name__ == '__main__':
    path = "keys-1130_8"
    keys_list = csv_util.read_csv(path + ".csv")
    time_key_dict = {}
    range_key_dict = {}
    for item in keys_list:
        # time_key_dict[item[1]] = 1 if item[1] not in time_key_dict.keys() else time_key_dict[item[1]] + 1
        range_key_dict[item[2]] = 1 if item[2] not in range_key_dict.keys() else range_key_dict[item[2]] + 1

    # res_range_key_dict = {}
    # keys_sort = sorted(range_key_dict)
    # for item in keys_sort:
    #     res_range_key_dict[item] = range_key_dict[item]
    # sorted(range_key_dict.)
    # sorted(time_key_dict)
    print(1)

    figure = plt.figure()
    # plt.subplot(121)
    plt.bar(range_key_dict.keys(), range_key_dict.values())
    plt.xlabel("Nums")
    plt.xticks([])
    plt.ylim(0, 20000)
    plt.ylabel("Range Key ID")

    # 画第4个图：条形图
    # plt.subplot(122)
    # plt.bar(time_key_dict.keys(), time_key_dict.values())
    # plt.xlabel("Nums")
    # plt.xticks([])
    # plt.ylabel("Time Key ID")

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.show()



