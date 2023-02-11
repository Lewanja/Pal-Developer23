from boolean_logic_interpreter import evaluate, func_not

s1 = "let X = F"
s2 = "let Y = ¬X"
s3 = "¬X ∧ Y"

variable_dict = {}


def replace_value_in_string(s):
    for variable_key, variable_value in variable_dict.items():
        print(f"variable key  is {variable_key}")
        if variable_key in s:
            print(f"variable {variable_key} is in string {s}")
            s = s.replace(variable_key, variable_value)
            print(f"new string is {s}")
    return s


def process_var_assign(s):
    if "let" in s:
        s_list = s.split(" ")
        declared_variable = s_list[1]
        variable_value = s_list[3]
        value = replace_value_in_string(variable_value)
        variable_dict[declared_variable] = value
        return variable_dict
    return None


def evaluate_variable_sub(s):
    if "¬F" in s:
        s = s.replace("¬F", "T")
    elif "¬T":
        s = s.replace("¬T", "F")
    else:
        evaluate()


print(f"before : {variable_dict}")
process_var_assign(s1)

print(f"after s1 : {variable_dict}")
process_var_assign(s2)
print(f"after s2 : {variable_dict}")

s3_solved = replace_value_in_string(s3)
print(f's3 solved is {s3_solved}')

s3_evaluated = evaluate(s3_solved.replace("¬F", "T"))
print(f"s3_evaluted = {s3_evaluated}")
