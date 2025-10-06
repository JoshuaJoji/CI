import os
import pandas as pd
import numpy as np
from synthetic_data import synthetic_data, synthetic_data_with_error
from best_fit_line import best_fit_line

def test_csv_exists():
    synthetic_data(filename="data.csv")
    assert os.path.exists("data.csv"), "CSV file was not created."

def test_plot_exists():
    synthetic_data(filename="data.csv")
    best_fit_line(filename="data.csv", plotname="Best_Line_Fit.png")
    assert os.path.exists("Best_Line_Fit.png"), "Plot file was not created."

def test_fit_accuracy():
    m_true, b_true = 2, 5
    X, Y = synthetic_data(m=m_true, b=b_true, filename="data.csv")
    m_fit, b_fit = best_fit_line(filename="data.csv", plotname="Best_Line_Fit.png")
    assert np.isclose(m_fit, m_true, atol=1.0), f"Slope not close: {m_fit} vs {m_true}"
    assert np.isclose(b_fit, b_true, atol=5.0), f"Intercept not close: {b_fit} vs {b_true}"

def test_csv_with_error_column():
    X, Y, errors = synthetic_data_with_error(filename="data_with_errors.csv")
    df = pd.read_csv("data_with_errors.csv")
    assert "Error" in df.columns, "Error column not found in CSV"
    assert len(df["Error"]) == len(X)