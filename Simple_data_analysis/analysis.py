import json
import pandas as pd
import sys


def analysis(file, user_id):
    try:
        user_id = int(user_id)
        df = pd.read_json(file)
        df_one = df[df['user_id'] == user_id]
    except ValueError:
        times = 0
        minutes = 0
        return times,minutes
    if df_one.empty:
        times = 0
        minutes = 0
        return times,minutes
    else:
        minutes = df_one['minutes'].sum()
        times = df_one['user_id'].count()
        return times,minutes



