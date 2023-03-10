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
    This should be called second after variable substitution
    it checks any brackets and solves those first before calling the evaluate function
    :param s: example s =(T ∨ F) = T
    :return: T = F
    """
    s = s.replace(" ", "")
    if "(" in s:
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

def evaluate_booleans_and_substitute(s):
    if "¬F" in s:
        s = s.replace("¬F", "T")
    if "¬T":
        s = s.replace("¬T", "F")
    return s


def evaluate_with_equality_check(s):
    if "=" in s:
        s = s.replace(" ", '')
        s_parts = s.split("=")
        left_expression = s_parts[0]
        right_expression = s_parts[1]
        left_result = evaluate_with_brackets(left_expression)
        right_result = evaluate_with_brackets(right_expression)
        return equal_operator(left_result, right_result)
    else:
        return evaluate_with_brackets(s)


def evaluate(s):
    """
    This function is always called last on the simplest forms of expressions
    It deals directly with the operators and returns a single variable i.e. T or F
    params:
        s : the string to be evaluated
    return result either of T or F
    raises
        InvalidOperatorException
        InvalidSymbolException
    """
    # convert everything to uppercase and remove spaces
    s = s.upper()
    s = s.replace(" ", '')
    # check if s is T or F and return it as is
    if s == 'T' or s == 'F':
        return s
    # first evaluate simple not expressions
    s = evaluate_booleans_and_substitute(s)

    # Determine the operator and variables
    boolean_operators = {"∨": or_operator, "∧": and_operator, "¬": func_not, "=": equal_operator}
    boolean_variables = {"T": 1, "F": 0}
    arguments = []
    s = list(s)
    operator = None
    for value in s:
        if value in boolean_variables:
            arguments.append(boolean_variables[value])
        elif value in boolean_operators:
            operator = boolean_operators[value]
        else:
            raise UnknownSymbolException(f"Symbol {value} in {s} is unkown. "\
                "Please ensure all variables are assigned and only the symbols below used.")
    if not operator:
        raise InvalidOperatorException
    result = operator(*arguments)
    return result


class InvalidOperatorException(Exception):
    """
    Raised when an operator supplied is not part of the supported list
    """
    pass


class UnknownSymbolException(Exception):
    """
    Raised when a symbol is not part of the recognised list
    """
    pass
