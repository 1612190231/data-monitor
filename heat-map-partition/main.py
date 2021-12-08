# -*- coding: utf-8 -*-
# Description: 热力图
# Created: luck 2021/09/15
import folium
import pandas as pd
import numpy as np
import webbrowser
from folium.plugins import HeatMap

if __name__ == '__main__':
    # 读取csv文件
    # data = csv_util.read_csv("../resources/test.csv")
    LOC = []
    lon_lst, lat_lst = [], []
    for i in range(1, 6):
        df = pd.read_csv("../resources/q" + str(i) + ".csv")
        # df = pd.read_csv("../resources/11.csv")
        df = df[["lat", "lon"]]
        lon_lst.extend(df['lon'].to_list())
        lat_lst.extend(df['lat'].to_list())
        # print(i)

    for lng, lat in zip(lon_lst, lat_lst):
        LOC.append([lat, lng])

    Center = [np.mean(np.array(lat_lst, dtype='float32')), np.mean(np.array(lon_lst, dtype='float32'))]
    m = folium.Map(location=Center, zoom_start=11,
                   max_lat=53.33, min_lat=3.51, max_lon=135.05, min_lon=73.33,
                   max_zoom=12, min_zoom=7)
    HeatMap(LOC).add_to(m)

    # 保存格式为html文件，可使用绝对路径进行保存
    name = 'ten_year_data.html'
    m.save(name)

    # 将结果文件打开进行显示
    webbrowser.open(name, new=2)
