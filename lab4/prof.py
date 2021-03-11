import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport

df=pd.read_csv('http://nbviewer.jupyter.org/github/Yorko/mlcourse_open/blob/master/data/mlbootcamp5_train.csv', sep=';', index_col='id')

profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("report.html")