# Utils
import numpy as np
import pandas as pd
import urllib.request
from tqdm import tqdm
pd.set_option('display.max_columns', None)

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Feature engineering
from sklearn.preprocessing import OrdinalEncoder

# Modelling
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


df = pd.read_csv('kc_house_data.csv')
print(df)