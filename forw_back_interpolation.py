import streamlit as st
import pandas as pd

def p_variable(x_list, x_forw, x_back):
    h = x_list[1] - x_list[0]
    p_forw = (x_forw - x_list[0]) / h
    p_back = (x_back - x_list[-1]) / h
    return p_forw, p_back

def difference_table(y_list):
    n = len(y_list)
    diff_table = [y_list]

    for i in range(1, n):
        next_row = []
        for j in range(n - i):
            diff = diff_table[i - 1][j + 1] - diff_table[i - 1][j]
            next_row.append(diff)
        diff_table.append(next_row)
    return diff_table

def forward_interpolation(p_forw, difference_list):
    y_o = difference_list[0][0]
    forward_interpolation_result = y_o
    p_forw_list = [1]

    for i in range(1, len(difference_list)):
        p_forw_term = p_forw_list[-1] * (p_forw - (i - 1)) / i
        p_forw_list.append(p_forw_term)

    factorial_list = [1]
    factorial = 1
    for i in range(1, len(difference_list)):
        factorial *= i
        factorial_list.append(factorial)

    for i in range(1, len(difference_list)):
        forward_interpolation_result += (p_forw_list[i] * difference_list[i][0]) / factorial_list[i]

    return forward_interpolation_result

def backward_interpolation(p_back, difference_list):
    y_n = difference_list[0][-1]
    backward_interpolation_result = y_n
    p_back_list = [1]

    for i in range(1, len(difference_list)):
        p_back_term = p_back_list[-1] * (p_back + (i - 1)) / i
        p_back_list.append(p_back_term)

    factorial_list = [1]
    factorial = 1
    for i in range(1, len(difference_list)):
        factorial *= i
        factorial_list.append(factorial)

    for i in range(1, len(difference_list)):
        backward_interpolation_result += (p_back_list[i] * difference_list[i][-1]) / factorial_list[i]

    return backward_interpolation_result

st.title("Forward and Backward Interpolation")
st.info("This app performs forward and backward interpolation using Newton's forward and backward interpolation methods.")

x_list = []
y_list = []

x_count = st.number_input("How many x values?", min_value=2, step=1, key="x_count")
y_count = x_count  # Ensuring the number of y values is the same as the number of x values

with st.form(key='data_points_form'):
    for i in range(x_count):
        col1, col2 = st.columns(2)
        with col1:
            x_val = st.number_input(f"Enter x[{i}]", key=f"x_{i}", step=1.,format="%.2f")
            x_list.append(x_val)
        with col2:
            y_val = st.number_input(f"Enter y[{i}]", key=f"y_{i}", step=1.,format="%.4f")
            y_list.append(y_val)

    x_forw = st.number_input("X value for forward interpolation", key="x_forw",step=1.,format="%.2f")
    x_back = st.number_input("X value for backward interpolation", key="x_back",step=1.,format="%.2f")
    submit_button = st.form_submit_button(label='Interpolate')

if submit_button:
    if len(set(x_list)) != len(x_list):
        st.error("x values must be distinct.")
    p_forw, p_back = p_variable(x_list, x_forw, x_back)
    difference_list = difference_table(y_list)
    forward_result = forward_interpolation(p_forw, difference_list)
    backward_result = backward_interpolation(p_back, difference_list)

    df_diff = pd.DataFrame(difference_list)
    transpose_df = df_diff.T

    st.write("Difference Table:")
    st.table(transpose_df)

    st.success(f"Value of Forward Interpolation: {forward_result}")
    st.success(f"Value of Backward Interpolation: {backward_result}")

st.caption("Made with ❤️ by Ashhad, Shaheer, Shahriyar, Mohsin, Emad, and Abdullah.")

