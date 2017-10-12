import pandas as pd

def  quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    volume = data['Volume']
    date = data['Date']
    volume.index = pd.to_datetime(date)
    vol = volume.resample('q').sum()
    second_volume = vol.sort_values()[-2]
    return second_volume

if __name__ == '__main__':
    quarter_volume()
