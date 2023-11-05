import unittest
from math_quiz import generate_random_number, select_random_math_operator, perform_math_operation


class TestMathQuiz(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_math_operator(self):
        # Test if random operator generated is within the chosen operators
        operator = select_random_math_operator()
        self.assertIn(operator, ['+', '-', '*'])

    def test_perform_math_operation(self):
        # Test if problem and answer are generated in the expected way
        test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, 3, '*', '2 * 3', 6),
                (0, 3, '*', '0 * 3', 0),
                (9, 7, '-', '9 - 7', 2)
            ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            actual_problem, actual_answer = perform_math_operation(num1, num2, operator)
            self.assertEquals(expected_problem, actual_problem)
            self.assertEquals(expected_answer, actual_answer)

if __name__ == "__main__":
    unittest.main()

