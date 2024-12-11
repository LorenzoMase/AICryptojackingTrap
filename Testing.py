import keras
import tensorflow as tf
import numpy as np
import pandas as pd
path_model='Path_Of_Model'
path_testing='Path_Of_testing_CSV'
path_testing1='Path_Of_secondTesting_CSV'
model = tf.keras.models.load_model(path_model)
dataset = pd.read_csv(path_testing)
x = dataset.drop(columns=["mining(1=M 0=nM)"])
y = dataset["mining(1=M 0=nM)"]
model.evaluate(x,y)

dataset1 = pd.read_csv(path_testing1)
x1 = dataset1.drop(columns=["mining(1=M 0=nM)"])
y1 = dataset1["mining(1=M 0=nM)"]
model.evaluate(x1,y1)
