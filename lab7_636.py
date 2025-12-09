def build_number_list(t_line):
    numbers_list = list(map(int, t_line.split()))
    return numbers_list

def unique_numbers(inp_list):
    no_duplic = list(set(inp_list))
    return no_duplic

input_line = input("Enter numbers: ")
initial_list = build_number_list(input_line) 
final_list = unique_numbers(initial_list)
print(final_list)