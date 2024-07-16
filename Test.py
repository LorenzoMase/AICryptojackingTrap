import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
dataset = pd.read_csv('dataset.csv')
#dataset contains the whole csv file, pandas permits the read
x = dataset.drop(columns=["label"])
y = dataset["label"]
#x contains all the feature's values, y contains all the real labels
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#Splitting the Data into trainingSet e testingSet, with a 1/5 relation"""
model = tf.keras.models.Sequential()
#Sequential model, optimized for 1 tensor input and 1 tensor output
model.add(tf.keras.layers.Dense(256, input_shape=x_train.shape[1:], activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
#Creation of the NN, parameters are casual for now, Dense should be the right kind of layer.
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#Definition of the model, with "adam" optimizer, crossentropy loss function, and accuracy as an output metric.
model.fit(x_train, y_train, epochs=1000)
model.evaluate(x_test, y_test)
#Training and evaluation.
