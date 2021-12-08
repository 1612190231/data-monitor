# -*- coding: utf-8 -*-
# Description: 手动绘制热力图分区
# Created: luck 2021/09/22
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # LOC = []
    lon_lst, lat_lst = [], []
    # for i in range(1, 6):
    name = "-1130"
    df = pd.read_csv("../resources/data/" + name + ".csv", names=["id", "utc", "lat", "lon"])
    # df = pd.read_csv("../resources/11.csv")
    df = df[["lat", "lon"]]
    lon_lst.extend(df['lon'].to_list())
    lat_lst.extend(df['lat'].to_list())
    print(1)

    # for lng, lat in zip(lon_lst, lat_lst):
    #     LOC.append([lat, lng])
    # # print(loc_n(2,'fac_seq_num.txt'))
    # fac_2 = loc_n(2, 'fac_seq_num.txt')
    # abe_2 = loc_n(2, 'abe_seq_num.txt')

    plt.scatter(lon_lst, lat_lst, marker='o', color='blue', label='loc', s=0.8, alpha=0.01)

    # plt.scatter([66], [49], marker='^', color='darkred', label='LCSD_2', s=8)

    # plt.title('Scatter')
    plt.title("scatter points", fontsize=18)
    plt.xlabel("lon", fontsize=9)
    plt.ylabel("lat", fontsize=9)
    plt.axis([73.33, 135.05, 3.51, 53.33])
    plt.legend(loc='upper right')
    # plt.xticks(fac_cpx_loc_2)
    # plt.yticks(abe_cpx_loc_2)
    plt.show()
    # plt.savefig('test.jpg')
