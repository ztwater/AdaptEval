import numpy as np
import pandas as pd
import scipy.stats as sps
from sklearn import linear_model
from sklearn.metrics import roc_curve, RocCurveDisplay, auc
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# define data distributions
N0 = 300
N1 = 250

dist0 = sps.gamma(a=8, scale=1/10)
x0 = np.linspace(dist0.ppf(0), dist0.ppf(1-1e-5), 100)
y0 = dist0.pdf(x0)

dist1 = sps.gamma(a=15, scale=1/10)
x1 = np.linspace(dist1.ppf(0), dist1.ppf(1-1e-5), 100)
y1 = dist1.pdf(x1)

with plt.style.context("bmh"):
    plt.plot(x0, y0, label="NEG")
    plt.plot(x1, y1, label="POS")
    plt.legend()
    plt.title("Gamma distributions")
