#Descobrir se havia mais mulheres ou homens entre os sobreviventes.

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanictrain = pd.read_csv(url)

print(titanictrain[['Sex']].describe())
