#!/usr/bin/env python3
"""function fill values with some procedures"""


def fill(df):
    """
    Removes the Weighted_Price column.
    xFills missing values in the Close column with the previous rows value.
    xFills missing values in the High, Low, and Open columns with the
    xcorresponding Close value in the same row.
    xSets missing values in Volume_(BTC) and Volume_(Currency) to 0.
    Returns: the modified pd.DataFrame.
    """
    df_new = df.drop(columns="Weighted_Price")
    df_new['Close'] = df['Close'].ffill()
    cols = ['High', 'Low', 'Open']  # for changing multiple columns at once
    df_new['High'] = df['High'].fillna(value=df_new['Close'])
    df_new['Low'] = df['Low'].fillna(value=df_new['Close'])
    df_new['Open'] = df['Open'].fillna(value=df_new['Close'])
    df_new['Volume_(BTC)'] = df_new['Volume_(BTC)'].fillna(value=0)
    df_new['Volume_(Currency)'] = df_new['Volume_(Currency)'].fillna(value=0)

    return df_new
