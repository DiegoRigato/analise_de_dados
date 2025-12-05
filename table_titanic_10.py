import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.cbook import boxplot_stats
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler,Normalizer


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanic = pd.read_csv(url)

le = LabelEncoder()

titanic['Ticket_codigo'] = le.fit_transform(titanic['Ticket'])

print(titanic.head(20))