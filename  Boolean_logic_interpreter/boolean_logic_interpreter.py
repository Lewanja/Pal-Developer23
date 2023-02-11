def or_operator(a, b):
    c = a + b
    # print(c)
    if c >= 1:
        return "T"
    else:
        return "F"


def and_operator(a, b):
    result = a * b
    if result == 1:
        return 'T'
    else:
        return 'F'


def func_not(a):
    if a == 0:
        return "T"
    else:
        return "F"


def equal_operator(a, b):
    if a == b:
        return "T"
    else:
        return "F"


def evaluate_with_brackets(s):
    """
    :param s: example s =(T ∨ F) = T
    :return: T = F
    """
    if "(" in s:
        s = s.replace(" ", "")
        bracket_one = s.index("(")
        bracket_two = s.index(")")
        brackets_expression = s[bracket_one: bracket_two + 1]
        string_without_brackets = s[bracket_one + 1:bracket_two]
        bracket_result = evaluate(string_without_brackets)
        evaluated_string = s.replace(brackets_expression, bracket_result)
        final_result = evaluate(evaluated_string)
        return final_result
    else:
        result = evaluate(s)
        return result


def evaluate(s):
    boolean_operators = {"∨": or_operator, "∧": and_operator, "¬": func_not, "=": equal_operator}
    boolean_variables = {"T": 1, "F": 0}
    arguments = []
    s = s.replace(" ", '')
    s = list(s)
    for value in s:
        if value in boolean_variables:
            arguments.append(boolean_variables[value])
            print(f" {value} is in {boolean_variables}")
        else:
            operators = boolean_operators[value]
            print(f" {value} is in {list(boolean_operators)}")

    result = operators(*arguments)
    print(f"The result for arguments is: {arguments}")
    return result
