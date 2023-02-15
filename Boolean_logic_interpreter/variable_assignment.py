from boolean_logic_interpreter import evaluate_with_equality_check


def replace_variables_in_string(s, variable_dict):
    for variable_key, variable_value in variable_dict.items():
        # print(f"variable key  is {variable_key}")
        if variable_key in s:
            # print(f"variable {variable_key} is in string {s}")
            s = s.replace(variable_key, variable_value)
            # print(f"new string is {s}")
    return s


def get_variables_in_line_of_code(s, variable_dict):
    if "let" in s:
        s_list = s.split(" ")
        declared_variable = s_list[1]
        variable_value = s_list[3]
        value = replace_variables_in_string(variable_value, variable_dict)
        variable_dict[declared_variable] = value
        return variable_dict
    return {}


def evaluate_with_variables(code_block):
    combined_variable_dict = {}
    all_lines_of_code = code_block.split("\n")

    # remove empty lines
    valid_lines_of_code = []
    for line in all_lines_of_code:
        line = line.strip()
        if line != "":
            valid_lines_of_code.append(line)

    lines_with_no_variables = []
    for line in valid_lines_of_code:
        if "let" in line:
            line_variable_dict = get_variables_in_line_of_code(line, combined_variable_dict)
            # combine initial variables and new ones obtained
            combined_variable_dict = {**combined_variable_dict, **line_variable_dict}
        else:
            line_with_no_variables = replace_variables_in_string(line, combined_variable_dict)
            lines_with_no_variables.append(line_with_no_variables)

    # now call evaluate on the lines with no variables
    evaluate_results = []
    for line in lines_with_no_variables:
        result = evaluate_with_equality_check(line)
        evaluate_results.append(result)


    # We ideally expect one result but to handle cases where the user might have entered multiple expressions we return a list
    if len(evaluate_results) == 1:
        return evaluate_results[0]
    else:
        return " ".join(evaluate_results)



code_block = """
let X = F
let Y = ¬X
let Z = T
(¬X ∧ Y)∨Z = F
"""

s = evaluate_with_variables(code_block)
print(s)

