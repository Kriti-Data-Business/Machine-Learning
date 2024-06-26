# Repeated K-Fold Cross-Validation

# #### Description
# - **Procedure**:
#   1. Perform K-Fold Cross-Validation multiple times with different random splits.
#   2. Each time, shuffle the dataset and divide into \( k \) folds.
#   3. Perform the entire K-Fold process \( n \) times.
#   4. Average the performance metrics over all \( k \times n \) iterations.

# #### Example
# - **Usage**: When you want a more robust estimate of model performance and have the computational resources to perform multiple rounds of cross-validation.
# - **Example**: You perform 5-Fold Cross-Validation 3 times (repeats = 3), resulting in 15 total training and testing iterations.


from sklearn.model_selection import RepeatedKFold

# Define Repeated K-Fold cross-validator
repeated_kfold = RepeatedKFold(n_splits=5, n_repeats=3, random_state=1)

# Evaluate the model
repeated_kfold_scores = cross_val_score(model, X, y, cv=repeated_kfold)

print("Accuracy scores for each fold: ", repeated_kfold_scores)
print("Mean accuracy: ", repeated_kfold_scores.mean())
