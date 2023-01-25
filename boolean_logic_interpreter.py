# # map symbols of or, and, not to their mathematical representations

# # map the variables to as using one and zero
# boolean_variables = {"A": 1, "B": 0}
# # write the final output of expected result from the variables
import unittest


def add(a, b):
    c = a + b
    # print(c)
    if c >= 1:
        return "True"
    else:
        return "False"


def multiply(a, b):
    result = a * b
    if result == 1:
        return 'True'
    else:
        return 'False'


def func_not(a):
    if a == 0:
        return "True"
    else:
        return "False"


# mult_func = multiply(1, 0)
# not_func = func_not("1")
# print(mult_func)
# print(not_func)


# print(boolean_operators["∨"])
# s = "(T∨F)"
# s = list(s)
# print(s)
#
# # check if string contains brackets
# for value in s:
#     if value == "(":
#         print(s[s.index("(") + 1:s.index(")")])
#         if value == "∨":
#             add()


# if it contains brackets evaluate by checking whether the not operation appears,
# division or whether the variables are products and perform operations


def evaluate(s):
    boolean_operators = {"∨": add, "∧": multiply, "¬": func_not}
    boolean_variables = {"T": 1, "F": 0}
    arguments = []
    s =s.split(" ")
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




class BooleanTest(unittest.TestCase):
    def test_or_with_true_true(self):
        actual = add(a=1, b=1)
        expected = "True"
        self.assertEqual(actual, expected)

    def test_or_with_true_false(self):
        actual = add(a=1, b=0)
        expected = "True"
        self.assertEqual(actual, expected)

    def test_or_with_false_true(self):
        actual = add(a=0, b=1)
        expected = "True"
        self.assertEqual(actual, expected)

    def test_or_with_false_false(self):
        actual = add(a=0, b=0)
        expected = "False"
        self.assertEqual(actual, expected)

    def test_and_with_false_false(self):
        actual = multiply(0, 0)
        expected = "False"
        self.assertEqual(actual, expected)

    def test_and_with_false_true(self):
        actual = multiply(0, 1)
        expected = "False"
        self.assertEqual(actual, expected)

    def test_and_with_true_false(self):
        actual = multiply(1, 0)
        expected = "False"
        self.assertEqual(actual, expected)

    def test_and_with_true_true(self):
        actual = multiply(1, 1)
        expected = "True"
        self.assertEqual(actual, expected)

    def test_not_false(self):
        actual = func_not(0)
        expected = "True"
        self.assertEqual(actual, expected)

    def test_not_true(self):
        actual = func_not(1)
        expected = "False"
        self.assertEqual(actual, expected)


class EvaluationTest(unittest.TestCase):
    def test_or_false_false_evaluation(self):
        actual = evaluate("F ∨ F")
        expected = "False"
        self.assertEqual(actual, expected)

