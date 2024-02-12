import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as scp
import plotly.express as px
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

df = pd.read_csv('motorcycle_specifications.csv')
totalrows, total_attributes = df.shape

print(f"Total Number of Rows: {totalrows}")
print(f"Total Number of Attributes: {total_attributes}")
print("================================================")
print(df.head())
print("================================================")
print(df.info())
print("================================================")
print(df.describe())
print("================================================")
print(df.describe(include=['object']))
print(df.describe(include=['float64']))
print("================================================")
