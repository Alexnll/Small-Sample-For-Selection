import pandas as pd
import numpy as np

data_path = '.\\ml-latest-small\\'
# 读取csv文件
movies = pd.read_csv(data_path + 'movies.csv')
ratings = pd.read_csv(data_path + 'ratings.csv')
tags = pd.read_csv(data_path + 'tags.csv')
#print(movies.head())
#print(ratings.head())
#print(tags.head())

# 合并movies与ratings并处理
movies_merged = pd.merge(movies, ratings, on='movieId')
movies_merged.drop(['userId', 'timestamp'], axis=1, inplace=True)
movies_merged = pd.merge(movies_merged.groupby('movieId')['rating'].mean(), movies_merged, on='movieId')
movies_merged.drop(['rating_y'], axis=1, inplace=True)
movies_merged.rename(columns={'rating_x':'ratings'}, inplace=True)
movies_merged.drop_duplicates(subset=['movieId', 'ratings'], keep='first', inplace=True)

# 合并tags
tags.drop(['userId', 'timestamp'], axis=1, inplace=True)
movies_merged = pd.merge(tags, movies_merged, on='movieId')
movies_merged.sort_values('movieId', inplace=True)
print(movies_merged.head())

# 输出
movies_merged.to_csv('movies_treated.csv', index=None)