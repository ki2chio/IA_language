import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 20)


df = pd.read_csv('https://raw.githubusercontent.com/susanli2016/Machine-Learning-with-Python/master/data/renfe_small.csv', sep=',')
print(df)