import numpy as np
import pandas as pd

import os

# 分隔输入用函数
def treat_input():
    # 用户输入
    user_input = input('Print movieId, tag, genres: ')
    return user_input.split(sep=' ')

def search(df, input_list):
    col_name = input_list[0]
    row_sel = input_list[1]
    print(df.loc[df[col_name] == row_sel])

if __name__ == '__main__':
    # 清屏
    os.system('cls')

    # 读取处理好的数据集
    movies_list = pd.read_csv('movies_treated.csv')
    print(movies_list.head(), '\n')
    
    # 用户输入
    input_list = treat_input()

    # 查找
    search(movies_list, input_list)