
### 2. Stratified K-Fold Cross-Validation

#### Description
# - **Procedure**: Same as K-Fold Cross-Validation but ensures that each fold maintains the class distribution of the original dataset.
# - **Advantage**: Useful for imbalanced datasets where some classes are underrepresented.

# #### Example
# - **Usage**: When dealing with classification tasks, especially with imbalanced classes.
# - **Example**: You have a dataset with a class distribution of 90% class A and 10% class B. Stratified K-Fold ensures each fold has approximately the same distribution.


from sklearn.model_selection import StratifiedKFold

# Define Stratified K-Fold cross-validator
stratified_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)

# Evaluate the model
stratified_scores = cross_val_score(model, X, y, cv=stratified_kfold)

print("Accuracy scores for each fold: ", stratified_scores)
print("Mean accuracy: ", stratified_scores.mean())
