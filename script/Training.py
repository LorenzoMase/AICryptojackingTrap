import pandas as pd
import numpy as np
import keras
from sklearn.model_selection import train_test_split
import tensorflow as tf
import os

csv_file='Path_Of_CSV'

def training(csv_file, output_path):
    dataset = pd.read_csv(csv_file, low_memory=False)
    x = dataset.drop(columns=["mining(1=M 0=nM)"])
    y = dataset["mining(1=M 0=nM)"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)
    x_train = np.asarray(x_train).astype('float64')
    x_test = np.asarray(x_test).astype('float64')

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(1033, activation='sigmoid'))
    model.add(tf.keras.layers.Dense(128, activation='sigmoid'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='BinaryCrossentropy', metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=20)
    model.evaluate(x_test, y_test)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    model.save(output_path)
