def input_values():
    x_count = int(input("How many x values? "))
    x_list = []
    for i in range(x_count):
        x = float(input(f"Enter x value for {i + 1}: "))
        x_list.append(x)
    print(x_list)
    
    y_count = int(input("How many y values? "))
    y_list = []
    for i in range(y_count):
        y = float(input(f"Enter y value for {i + 1}: "))
        y_list.append(y)
    print(y_list)

    return x_list, y_list


def p_variable(x_list):
    x_forw = float(input("X value for forward interpolation: "))
    x_back = float(input("X value for backward interpolation: "))
    h_list = []
    for i in range(len(x_list) - 1):
        difference = x_list[i + 1] - x_list[i]
        h_list.append(round(difference, 2))

    if h_list[-1] == 0:
        print("Invalid value for difference")
    elif h_list[-1] != h_list[-2]:
        print("Invalid difference")
    else:
        h = h_list[0]
        p_forw = (x_forw - x_list[0]) / h
        p_forw = round(p_forw, 2)
        p_back = (x_back - x_list[-1]) / h
        p_back = round(p_back, 2)
        print("h_list:", h_list)
        print("h_value:", h)
        print("p_forw:", p_forw)
        print("p_back:", p_back)
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
    print(f"Difference Table: {diff_table}")
    print(f"Difference table length: {len(diff_table)}")
    return diff_table


def forward_interpolation(p_forw, difference_list):
    y_o = difference_list[0][0]
    forward_interpolation_result = y_o
    p_forw_list = [1]

    for i in range(1, len(difference_list)):
        p_forw_term = p_forw_list[-1] * (p_forw - (i - 1)) / i
        p_forw_list.append(p_forw_term)

    print(f"Value of p forwards: {p_forw_list}")

    factorial_list = [1]
    factorial = 1
    for i in range(1, len(difference_list)):
        factorial *= i
        factorial_list.append(factorial)
    print(f"Factorial list: {factorial_list}")

    for i in range(1, len(difference_list)):
        forward_interpolation_result += (p_forw_list[i] * difference_list[i][0]) / factorial_list[i]

    print(f"Value of Forward Interpolation: {forward_interpolation_result}")
    return forward_interpolation_result


def backward_interpolation(p_back, difference_list):
    y_o = difference_list[0][-1]
    backward_interpolation_result = y_o
    p_back_list = [1]

    for i in range(1, len(difference_list)):
        p_back_term = p_back_list[-1] * (p_back + (i - 1)) / i
        p_back_list.append(p_back_term)

    print(f"Value of p backwards: {p_back_list}")

    factorial_list = [1]
    factorial = 1
    for i in range(1, len(difference_list)):
        factorial *= i
        factorial_list.append(factorial)
    print(f"Factorial list: {factorial_list}")

    for i in range(1, len(difference_list)):
        backward_interpolation_result += (p_back_list[i] * difference_list[i][-1]) / factorial_list[i]

    print(f"Value of Backward Interpolation: {backward_interpolation_result}")
    return backward_interpolation_result


x_list, y_list = input_values()
p_forw, p_back = p_variable(x_list)
difference_list = difference_table(y_list)
forwards_result = forward_interpolation(p_forw, difference_list)
backwards_result = backward_interpolation(p_back, difference_list)
