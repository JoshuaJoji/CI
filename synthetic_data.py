import numpy as np
import pandas as pd

def synthetic_data(m=2, b=5, num_points=100, filename="data.csv"):
    X = np.linspace(0, 100, num_points)
    Y = m * X + b   # exactly on the line, no noise

    # Save to CSV
    df = pd.DataFrame({"X": X, "Y": Y})
    df.to_csv(filename, index=False)

    return X, Y

def synthetic_data_with_error(m=2, b=5, num_points=100, noise_std=1.0, filename="data_with_errors.csv"):
    X = np.linspace(0, 100, num_points)
    Y_true = m * X + b
    
    noise = np.random.normal(0, noise.std, num_points)
    Y_noisy = Y_true + noise
    
    errors = np.random.uniform(0.5, 2.0, num_points)

    df = pd.DataFrame({"X": X, "Y": Y_noisy, "Error": errors})
    df.to_csv(filename, index=False)
    return X, Y_noisy, errors

if __name__ == "__main__":
    synthetic_data()