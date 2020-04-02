from csv import reader
import numpy as np
import matplotlib.pyplot as plt

def calculateOutput(order, thetaValues, x, y):
    output = 0

    for i in range(order + 1):
        if i == 0:
            output += thetaValues[0]
        else:
            output += thetaValues[i] * (x ** i)

    return output

def weightUpdate(order, thetaValues, x, y, output, alpha):
    for i in range(order + 1):
        thetaValues[i] = thetaValues[i] - alpha * (output - y) * np.power(x, i)
    
    return thetaValues

# function to calculate mean squared error
def calculateError(trainingData, thetaValues, order):
    errors = []
    for i in range(0, 100):
        x = float(trainingData[i][0])
        y = float(trainingData[i][1])

        predictedOutput = calculateOutput(order, thetaValues, x, y)
        actualOutput = float(trainingData[i][1])

        errors.append(np.power(predictedOutput - actualOutput, 2))
    error = sum(errors) / len(errors)
    return error

# read csv file as list of lists
with open('synthetic-1.csv', 'r') as read:
    csv_reader = reader(read)
    # create trainingData variable to hold list of lists
    trainingData = list(csv_reader)
    print(trainingData)

alpha = 0.01

# loop through training data and check errors for order = 1
thetaValues = [1, 1, 1, 1, 1, 1, 1, 1]
order = 1
for i in range(100):
    x = float(trainingData[i][0])
    y = float(trainingData[i][1])

    output = calculateOutput(order, thetaValues, x, y)
    thetaValues = weightUpdate(order, thetaValues, x, y, output, alpha)

    currentError = calculateError(trainingData, thetaValues, order)
    print("error for order = 1: " + str(currentError))

functionResult = []
trainingX = []

# 100 linearly spaced numbers
x = np.linspace(-2,2,100)
#functionResult2 = 
for j in range(100):
    trainingX.append(float(trainingData[i][0]))
    functionResult.append(thetaValues[0] + thetaValues[1] * float(trainingData[i][0]))

plt.plot(x,functionResult, 'r')

print("theta values for order = 1: " + str(thetaValues))

# loop through training data and check errors for order = 2
thetaValues = [1, 1, 1, 1, 1, 1, 1, 1]
order = 2
for i in range(100):
    x = float(trainingData[i][0])
    y = float(trainingData[i][1])

    output = calculateOutput(order, thetaValues, x, y)
    thetaValues = weightUpdate(order, thetaValues, x, y, output, alpha)

    currentError = calculateError(trainingData, thetaValues, order)
    print("error for order = 2: " + str(currentError))

print("theta values for order = 2: " + str(thetaValues))

functionResult2 = []
trainingX = []

# 100 linearly spaced numbers
x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)

for j in np.arange(-2, 2, 0.04):
    trainingX.append(float(trainingData[i][0]))
    functionResult2.append(thetaValues[0] + thetaValues[1] * j + thetaValues[2] * np.power(j, 2))
    #functionResult2.append(calculateOutput(3, thetaValues, x, y))

# plot the function
plt.plot(x,functionResult2, 'g')

# loop through training data and check errors for order = 4
thetaValues = [1, 1, 1, 1, 1, 1, 1, 1]
order = 4
for i in range(100):
    x = float(trainingData[i][0])
    y = float(trainingData[i][1])

    output = calculateOutput(order, thetaValues, x, y)
    thetaValues = weightUpdate(order, thetaValues, x, y, output, alpha)

    currentError = calculateError(trainingData, thetaValues, order)
    print("error for order = 4: " + str(currentError))

print("theta values for order = 4: " + str(thetaValues))

functionResult3 = []
trainingX = []

# 100 linearly spaced numbers
x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)
#functionResult2 = 
for j in np.arange(-2, 2, 0.04):
    trainingX.append(float(trainingData[i][0]))
    functionResult3.append(thetaValues[0] + thetaValues[1] * j + thetaValues[2] * np.power(j, 2) + thetaValues[3] * np.power(j, 3) + thetaValues[4] * np.power(j, 4))
    #functionResult3.append(calculateOutput(4, thetaValues, x[j], y))

# plot the function
plt.plot(x,functionResult3, 'b')

# loop through training data and check errors for order = 7
thetaValues = [1, 1, 1, 1, 1, 1, 1, 1]
order = 7
for i in range(100):
    x = float(trainingData[i][0])
    y = float(trainingData[i][1])

    output = calculateOutput(order, thetaValues, x, y)
    thetaValues = weightUpdate(order, thetaValues, x, y, output, alpha)

    currentError = calculateError(trainingData, thetaValues, order)
    print("error for order = 7: " + str(currentError))

print("theta values for order = 7: " + str(thetaValues))

functionResult4 = []
trainingX = []

# 100 linearly spaced numbers
x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)
#functionResult2 = 
for j in np.arange(-2, 2, 0.04):
    trainingX.append(float(trainingData[i][0]))
    functionResult4.append(thetaValues[0] + thetaValues[1] * j + thetaValues[2] * np.power(j, 2) + thetaValues[3] * np.power(j, 3) + thetaValues[4] * np.power(j, 4) + thetaValues[5] * np.power(j, 5) + thetaValues[6] * np.power(j, 6) + thetaValues[7] * np.power(j, 7))
    #functionResult3.append(calculateOutput(4, thetaValues, x[j], y))

# plot the function
# plt.plot(x,functionResult4, 'p')

test_array = np.array(trainingData)

plt.scatter(test_array[:, 0], test_array[:, 1], color = "black")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Synthetic Data 1")

plt.show()