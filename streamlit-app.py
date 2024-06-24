import streamlit as st
import forw_back_interpolation as flt
import matplotlib.pyplot as plt

# Title of the app
st.title("Forward and Backward Interpolation")

# Inputs
x_count = st.number_input("How many x values?", min_value=1, step=1, value=5)
x_list = []
y_list = []

for i in range(x_count):
    x = st.text_input(f"Enter x value {i+1}", key=f"x_{i}")
    x_list.append(float(x) if x else 0.0)

for i in range(x_count):
    y = st.text_input(f"Enter y value {i+1}", key=f"y_{i}")
    y_list.append(float(y) if y else 0.0)

x_forw = st.text_input("X value for forward interpolation")
x_back = st.text_input("X value for backward interpolation")

# Perform interpolation calculations
if st.button("Calculate"):
    p_forw, p_back = flt.p_variable(x_list)
    difference_list = flt.difference_table(y_list)
    forwards_result = flt.forward_interpolation(float(x_forw), difference_list)
    backwards_result = flt.backward_interpolation(float(x_back), difference_list)
    
    # Display the results
    st.write(f"Forward Interpolation Result: {forwards_result}")
    st.write(f"Backward Interpolation Result: {backwards_result}")

    # Plotting the results
    fig, ax = plt.subplots()
    ax.plot(x_list, y_list, 'bo-', label='Data points')
    ax.axvline(x=float(x_forw), color='r', linestyle='--', label=f'Forward Interpolation at x={x_forw}')
    ax.axvline(x=float(x_back), color='g', linestyle='--', label=f'Backward Interpolation at x={x_back}')
    ax.legend()
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")
    ax.set_title("Forward and Backward Interpolation")

    # Show the plot
    st.pyplot(fig)
