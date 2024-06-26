# 1. K-Fold Cross-Validation

# Certainly! Cross-validation techniques vary in how they split the data and how many iterations they perform. Here are the main types, their differences, and examples of when each might be used:

# ### 1. K-Fold Cross-Validation

# #### Description
# - **Procedure**:
#   1. Divide the dataset into \( k \) equal-sized folds.
#   2. Perform \( k \) iterations of training and testing.
#   3. In each iteration, one fold is used as the test set, and the remaining \( k-1 \) folds are used as the training set.
#   4. Average the performance metrics over the \( k \) iterations.

# #### Example
# - **Usage**: When you have a moderate-sized dataset and want a balanced estimate of model performance.
# - **Example**: You have 1000 samples and use 5-Fold Cross-Validation (i.e., \( k = 5 \)). Each fold contains 200 samples. 
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SYNTAX :CODE


from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load dataset
X, y = load_iris(return_X_y=True)

# Define the model
model = DecisionTreeClassifier()

# Define K-Fold cross-validator
kfold = KFold(n_splits=5, shuffle=True, random_state=1)

# Evaluate the model
scores = cross_val_score(model, X, y, cv=kfold)

print("Accuracy scores for each fold: ", scores)
print("Mean accuracy: ", scores.mean())
