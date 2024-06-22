def input_values():
     x_count = int(input("How many x values? "))
     x_list = []
     for i in range(x_count):
         x = float(input(f"Enter x value for {i+1}: "))
         x_list.append(x)
     print(x_list)
    
     y_count = int(input("How many y values? "))
     y_list = []
     for i in range(y_count):
         y = float(input(f"Enter y value for {i+1}: "))
         y_list.append(y)
     print(y_list)

     return x_list,y_list


def p_variable(x_list):
     x_forw = float(input("X value for forward interpolation: "))
     x_back = float(input("X value for backward interpolation: "))
     h = []
     for i in range(len(x_list) - 1):
         difference = x_list[i+1] - x_list[i]
         h.append(difference)
         if h[-1] == 0:
             print("Invalid value for difference")
         elif h[-1] != h[0]:
             print("Invalid difference")
         else:
             h_value = h[0]
        
     p_forw = (x_forw - x_list[0]) / h_value
     p_back = (x_back - x_list[-1]) / h_value
     print("h_value:", h_value)
     print("p_forw:", p_forw)
     print("p_back:", p_back)

def difference_table(y_list):
     y_diff_list = []
     for i in range(len(y_list) - 1):
        y_2 = y_list[i+1] - y_list[i]
        y_diff_list.append(y_2)
        print(f"Value for i: {i}")
        print(f"Value for x: {y_diff_list[i]}")

        



x_list, y_list = input_values()
difference_table(x_list, y_list)
p_variable(x_list)



