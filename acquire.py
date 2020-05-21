import pandas as pd
import numpy as np


def wrangle_logs_for_time_series():
    colnames=['date', 'time_stamp', 'destination', 'user_id', 'cohort', 'ip_address']
    df_orig = pd.read_csv('curriculum-access.txt',          
                 engine='python',
                 header=None,
                 index_col=False,
                 names=colnames,
                 sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',     
                 na_values='"-"')
    df_orig['ds'] = df_orig.date + ' ' + df_orig.time_stamp
    df_orig['ds'] = pd.to_datetime(df_orig['ds'])
    df_orig = df_orig.sort_values('ds').set_index('ds')
    df_orig = df_orig.drop(columns=(['date', 'time_stamp']))
    df_orig = df_orig.fillna(method='bfill')
    return df_orig




def wrangle_logs_for_clustering():
    colnames=['date', 'time_stamp', 'destination', 'user_id', 'cohort', 'ip_address']
    df_orig = pd.read_csv('curriculum-access.txt',          
                 engine='python',
                 header=None,
                 index_col=False,
                 names=colnames,
                 sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',     
                 na_values='"-"')
    df_orig['ds'] = df_orig.date + ' ' + df_orig.time_stamp
    df_orig['ds'] = pd.to_datetime(df_orig['ds'])
    df_orig = df_orig.drop(columns=(['date', 'time_stamp']))
    df_orig = df_orig.fillna(method='bfill')
    return df_orig