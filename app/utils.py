import pandas as pd

def load_data():
    datasets = {
        "Benin": pd.read_csv("data/benin-malanville.csv"),
        "Sierra Leone": pd.read_csv("data/sierraleone-bumbuna.csv"),
        "Togo": pd.read_csv("data/togo-dapaong_qc.csv"),
    }
    return datasets

def clean_data(df):
    df.fillna(method="ffill", inplace=True)
    df = df[df["GHI"] >= 0]
    return df
