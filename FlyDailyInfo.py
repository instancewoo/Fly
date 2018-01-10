#!/usr/bin/python
import numpy as np
import pandas as pd
from pandas import Series

DAILY_LIMIT_P = 9.8  # 涨幅，实际上涨停应大于此数值
DAY_COL_KEY_HIGH = 'high'
DAY_COL_KEY_LOW = 'low'
DAY_COL_KEY_P = 'p_change'
DAY_COL_KEY_DATE = 'date'
DAY_COL_KEY_HLA_NUM = 'high_limit_along_num'


# 根据一字板涨停条件抽取出一个df[date] 生成series 然后进行count，在将series根据date count 添加到原df
def get_daily_limit_along_factor(df):
    date_col_df = df[np.logical_and(df[DAY_COL_KEY_HIGH] == df[DAY_COL_KEY_LOW],
                                    df[DAY_COL_KEY_P] > DAILY_LIMIT_P)][DAY_COL_KEY_DATE]
    date_series = Series(date_col_df)
    # 这个series包含了每个date中的一字板个数
    date_num_series = date_series.value_counts()
    date_num_df = {DAY_COL_KEY_DATE: date_num_series.index,
                   DAY_COL_KEY_HLA_NUM: date_num_series.values}
    # 默认根据date作为两个表的key值进行连接合并
    return pd.merge(df, date_num_df)


if __name__ == '__main__':
    print("hello")
