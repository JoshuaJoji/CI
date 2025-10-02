import numpy as np
import pandas as pd

def synthetic_data(m=2, b=5, num_points=100, filename="data.csv"):
    X = np.linspace(0, 100, num_points)
    Y = m * X + b   # exactly on the line, no noise

    # Save to CSV
    df = pd.DataFrame({"X": X, "Y": Y})
    df.to_csv(filename, index=False)

    return X, Y

if __name__ == "__main__":
    synthetic_data()