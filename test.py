import unittest
from arithmetic_arranger import arithmetic_arranger

class UnitTests(unittest.TestCase):
    def test_valid_problems_without_answers(self):
        problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
        expected_result = (
            "   32      3801      45      123\n"
            "+ 698    -    2    + 43    +  49\n"
            "-----    ------    ----    -----"
        )
        self.assertEqual(arithmetic_arranger(problems), expected_result)

    def test_valid_problems_with_answers(self):
        problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
        expected_result = (
            "  32         1      9999      523\n"
            "+  8    - 3801    + 9999    -  49\n"
            "----    ------    ------    -----"
        )
        self.assertEqual(arithmetic_arranger(problems, True), expected_result)

    def test_too_many_problems_error(self):
        problems = ["1 + 1", "2 + 2", "3 + 3", "4 + 4", "5 + 5", "6 + 6"]
        expected_error = "Error: Too many problems."
        self.assertEqual(arithmetic_arranger(problems), expected_error)

    def test_invalid_operator_error(self):
        problems = ["1 + 1", "2 * 2"]
        expected_error = "Error: Operator must be '+' or '-'."
        self.assertEqual(arithmetic_arranger(problems), expected_error)

    def test_invalid_digit_error(self):
        problems = ["123 + abc", "456 - def"]
        expected_error = "Error: Numbers must only contain digits."
        self.assertEqual(arithmetic_arranger(problems), expected_error)

    def test_invalid_digit_length_error(self):
        problems = ["1234 + 5678", "9876 - 54321"]
        expected_error = "Error: Numbers cannot be more than four digits."
        self.assertEqual(arithmetic_arranger(problems), expected_error)

if __name__ == "__main__":
    unittest.main()
