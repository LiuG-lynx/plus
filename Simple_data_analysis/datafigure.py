import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json('~/Code/user_study.json')
df1 = df[['user_id','minutes']].groupby('user_id').sum()
ax = df1.plot(title='StudyData')
ax.set_ylabel('Study Time')
ax.set_xlabel('User ID')
plt.show()

