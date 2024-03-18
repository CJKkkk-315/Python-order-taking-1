import pandas as pd
from sklearn.neural_network import MLPRegressor
from pandas import DataFrame

import matplotlib.pyplot as plt
# Create Neural Net MLP regressor
# Explore settings logarithmically (0.1, 0.01, 0.001, 0.00001)
model = MLPRegressor(
    # try some layer & node sizes
    hidden_layer_sizes=(5,17),
    # find a learning rate?
    learning_rate_init=.001,
    # activation functions (relu, tanh, identity)
    activation='relu',
    max_iter=1
);
import csv
x = []
y = []
with open('新建文本文档.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        x.append(row[:9])
        y.append(row[-1])
X = DataFrame(x)
Y = DataFrame(y)
model.fit(X,Y)
pd.DataFrame(model.loss_curve_).plot()
plt.show()