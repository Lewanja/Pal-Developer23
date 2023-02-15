import unittest

from boolean_logic_interpreter import and_operator, func_not, evaluate, or_operator, evaluate_with_brackets, equal_operator
from variable_assignment import replace_value_in_string, process_var_assign, evaluate_variable_sub

class BooleanTest(unittest.TestCase):
    def test_or_with_true_true(self):
        actual = or_operator(a=1, b=1)
        expected = "T"
        self.assertEqual(actual, expected)

    def test_or_with_true_false(self):
        actual = or_operator(a=1, b=0)
        expected = "T"
        self.assertEqual(actual, expected)

    def test_or_with_false_true(self):
        actual = or_operator(a=0, b=1)
        expected = "T"
        self.assertEqual(actual, expected)

    def test_or_with_false_false(self):
        actual = or_operator(a=0, b=0)
        expected = "F"
        self.assertEqual(actual, expected)

    def test_and_with_false_false(self):
        actual = and_operator(0, 0)
        expected = "F"
        self.assertEqual(actual, expected)

    def test_and_with_false_true(self):
        actual = and_operator(0, 1)
        expected = "F"
        self.assertEqual(actual, expected)

    def test_and_with_true_false(self):
        actual = and_operator(1, 0)
        expected = "F"
        self.assertEqual(actual, expected)

    def test_and_with_true_true(self):
        actual = and_operator(1, 1)
        expected = "T"
        self.assertEqual(actual, expected)

    def test_not_false(self):
        actual = func_not(0)
        expected = "T"
        self.assertEqual(actual, expected)

    def test_not_true(self):
        actual = func_not(1)
        expected = "F"
        self.assertEqual(actual, expected)

    def test_equal_true_true(self):
        actual = equal_operator("T", "T")
        expected = "T"
        self.assertEqual(actual, expected)

    def test_equal_false_false(self):
        actual = equal_operator("F", "F")
        expected = "T"
        self.assertEqual(actual, expected)

    def test_equal_true_false(self):
        actual = equal_operator("T", "F")
        expected = "F"
        self.assertEqual(actual, expected)

    def test_equal_false_true(self):
        actual = equal_operator("F", "T")
        expected = "F"
        self.assertEqual(actual, expected)


class EvaluationTest(unittest.TestCase):
    def test_or_false_false_evaluation(self):
        actual = evaluate("F ∨ F")
        expected = "F"
        self.assertEqual(actual, expected)

    def test_or_false_true_evaluation(self):
        actual = evaluate("F ∨ T")
        expected = "T"
        self.assertEqual(actual, expected)

    def test_or_true_false_evaluation(self):
        actual = evaluate("T ∨ F")
        expected = "T"
        self.assertEqual(actual, expected)

    def test_or_true_true_evaluation(self):
        actual = evaluate("T ∨ T")
        expected = "T"
        self.assertEqual(actual, expected)

    def test_and_false_false_evaluation(self):
        actual = evaluate("F ∧ F")
        expected = "F"
        self.assertEqual(actual, expected)

    def test_and_false_true_evaluation(self):
        actual = evaluate("F ∧ T")
        expected = "F"
        self.assertEqual(actual, expected)

    def test_and_true_false_evaluation(self):
        actual = evaluate("T ∧ F")
        expected = "F"
        self.assertEqual(actual, expected)

    def test_and_false_false_evaluation(self):
        actual = evaluate("T ∧ T")
        expected = "T"
        self.assertEqual(actual, expected)

    def test_not_evaluation_f(self):
        actual = evaluate("¬T")
        expected = "F"
        self.assertEqual(actual, expected)

    def test_not_evaluation_t(self):
        actual = evaluate("¬F")
        expected = "T"
        self.assertEqual(actual, expected)


class BracketsTest(unittest.TestCase):
    def test_and_bracket(self):
        actual = evaluate_with_brackets("(T ∧ F) = F")
        expected = "T"
        self.assertEqual(actual, expected)

class ReplaceValueInStringTest(unittest.TestCase):
    def test_replace_value_in_string(self):
        actual = replace_value_in_string("let X = F")
        expected = pass