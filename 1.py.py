import numpy as np
weights = np.array([0.5, 0.48, -0.7])
alpha = 0.1

streetlights = np.array([[1, 0, 1],
                         [0, 1, 1],
                         [0, 0, 1],
                         [1, 1, 1],
                         [0, 1, 1],
                         [1, 0, 1]])

walk_vs_stop = np.array([0, 1, 0, 1, 1, 0])

input = streetlights[0] # [1, 0, 1]
goal_prediction = walk_vs_stop[0] # содержит 0 (стоять)

for iteration in range(20):
    prediction = input.dot(weights)
    error = (prediction - goal_prediction) ** 2
    delta = prediction - goal_prediction
    weights = weights - (alpha*(delta*input))

    print("Error: ", error, "Prediction: ", prediction)
    print(weights, delta)