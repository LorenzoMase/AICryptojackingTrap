import keras
import tensorflow as tf
import numpy as np
import pandas as pd
import os

def testing(model_path, testing_path):
    model = tf.keras.models.load_model(model_path)
    dataset = pd.read_csv(testing_path)
    x = dataset.drop(columns=["mining(1=M 0=nM)"])
    y = dataset["mining(1=M 0=nM)"]
    model.evaluate(x,y)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(base_dir,"../models")
    model_filename = "AICryptojackingTrapModel.keras"
    model_path = os.path.join(model_dir, model_filename)

    testing_dir = os.path.join(base_dir,"../csv")
    testing_filename = "normalized_data_testing.csv"
    testing_path = os.path.join(testing_dir, testing_filename)
    testing(model_path, testing_path)