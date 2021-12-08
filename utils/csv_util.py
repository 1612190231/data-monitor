# -*- coding: utf-8 -*-
# Description: excel操作类
# Created: luchengkai 2021/08/013

import csv
import openpyxl


def read_csv(read_path):
    """
    读取数据，定义数据读取csv函数
    :param read_path:  List[String]
    :return reader: List[List[]]
    """
    # 读取数据
    result_list =[]
    with open(read_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for item in reader:
            result_list.append(item)
        return result_list


def insert_csv(title_list, insert_list, insert_path):
    """
    空表写入，定义空表写入csv函数
    :param title_list:  List[String]
    :param insert_list: List[Tuple()]
    :param insert_path: String
    """
    with open(insert_path, 'w', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(title_list)     # 写入表头

        for data in insert_list:
            for tuple_item in data:
                csv_writer.writerow(list(tuple_item))


if __name__ == '__main__':
    print(1)
