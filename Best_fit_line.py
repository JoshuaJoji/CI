import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def best_fit_line(filename="data.csv", plotname="Best_Line_Fit.png"):
    df = pd.read_csv(filename)
    X = df["X"].values
    Y = df["Y"].values

    # slope (m), intercept (b)
    m_fit, b_fit = np.polyfit(X, Y, 1)

    # Plot the line + points
    plt.scatter(X, Y, label="Data")
    plt.plot(X, m_fit*X + b_fit, color='red', label="Best Fit Line")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Best Fit Line")
    plt.legend()
    plt.savefig(plotname)

    return m_fit, b_fit

if __name__ == "__main__":
    m, b = best_fit_line()
    print(f"Slope: {m:.2f}, Intercept: {b:.2f}")