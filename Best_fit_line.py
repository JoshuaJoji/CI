import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def best_fit_line(filename="data.csv", plotname="Best_Line_Fit.png"):
    df = pd.read_csv(filename)
    X = df["X"].values
    Y = df["Y"].values
    errors = df["Error"].values if "Error" in df.columns else None

    if errors is not None:
        weights = 1 / (errors**2)
        m_fit, b_fit = np.polyfit(X, Y, 1, w=weights)
    else:
        m_fit, b_fit = np.polyfit(X, Y, 1)

    if errors is not None:
        plt.errorbar(X, Y, yerr=errors, fmt="o", capsize=3, label="Data with error")
    else:
        plt.scatter(X, Y, label="Data")

    plt.plot(X, m_fit * X + b_fit, color="red", label="Best Fit Line")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Best Fit Line")
    plt.legend()
    plt.savefig(plotname)
    plt.close()

    return m_fit, b_fit