import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    return data

def preprocess(data):
    
    X = data.drop("result", axis=1)
    y = data["result"]

    return X, y
