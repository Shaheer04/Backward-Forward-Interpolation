import streamlit as st
import numpy as np

# Function for Newton's Forward Interpolation
def newton_forward_interpolation(x_values, y_values, x):
    n = len(x_values)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    h = x_values[1] - x_values[0]
    p = (x - x_values[0]) / h
    y_interp = y_values[0]
    p_product = 1

    for i in range(1, n):
        p_product *= (p - (i - 1))
        y_interp += (p_product * diff_table[0][i]) / np.math.factorial(i)

    return y_interp

# Function for Newton's Backward Interpolation
def newton_backward_interpolation(x_values, y_values, x):
    n = len(x_values)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]

    h = x_values[1] - x_values[0]
    p = (x - x_values[-1]) / h
    y_interp = y_values[-1]
    p_product = 1

    for i in range(1, n):
        p_product *= (p + (i - 1))
        y_interp += (p_product * diff_table[n - 1][i]) / np.math.factorial(i)

    return y_interp

# Streamlit app
def main():
    st.title("Newton's Forward and Backward Interpolation")

    n = st.number_input("Enter the number of data points", min_value=2, step=1)
    
    x_values = []
    y_values = []
    
    with st.form(key='data_points_form'):
        for i in range(n):
            col1, col2 = st.columns(2)
            with col1:
                x_val = st.number_input(f"Enter x[{i}]", key=f"x_{i}", step=1.,format="%.2f")
                x_values.append(x_val)
            with col2:
                y_val = st.number_input(f"Enter y[{i}]", key=f"y_{i}", step=1.,format="%.4f")
                y_values.append(y_val)
        
        x_to_interpolate = st.number_input("Enter the value of x to interpolate", key="x_interp", step=1.,format="%.2f")

        submit_button = st.form_submit_button(label='Interpolate')

    if submit_button:
        if len(set(x_values)) != len(x_values):
            st.error("x values must be distinct.")
        else:
            forward_result = newton_forward_interpolation(x_values, y_values, x_to_interpolate)
            backward_result = newton_backward_interpolation(x_values, y_values, x_to_interpolate)

            st.success(f"Forward Interpolation result at x = {x_to_interpolate}: {forward_result}")
            st.success(f"Backward Interpolation result at x = {x_to_interpolate}: {backward_result}")

if __name__ == "__main__":
    main()