### 5. Time Series Cross-Validation (Rolling Forecast Origin)

#### Description
# - **Procedure**:
#   1. Train the model on an increasing time span and test it on the next time step.
#   2. Move the training window forward and repeat.
#   3. This respects the temporal order of the data.

# #### Example
# - **Usage**: When dealing with time series data where future values should not be used to predict past values.
# - **Example**: You have a dataset with daily stock prices. Train on the first 10 days, test on day 11. Then train on days 1-11, test on day 12, and so on.



from sklearn.model_selection import TimeSeriesSplit

# Define Time Series cross-validator
time_series_split = TimeSeriesSplit(n_splits=5)

# Example dataset for time series (dummy data)
import numpy as np
X = np.arange(100).reshape((100, 1))
y = np.arange(100)

# Evaluate the model (Time series data)
for train_index, test_index in time_series_split.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print("Train indices:", train_index, "Test indices:", test_index, "Score:", score)
