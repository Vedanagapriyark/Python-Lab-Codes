from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Simple dataset: [height, weight], label: 0 = child, 1 = adult
X = [[120, 30], [130, 35], [160, 55], [170, 60]]  # Features
y = [0, 0, 1, 1]  # Labels (0 = child, 1 = adult)

# Create and train the model using 'entropy'
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# Plot the decision tree
plt.figure(figsize=(6, 4))
plot_tree(model, feature_names=["Height", "Weight"], class_names=["Child", "Adult"], filled=True)
plt.title("Simple Decision Tree (Entropy)")
plt.show()
