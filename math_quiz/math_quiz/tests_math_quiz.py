import unittest
from math_quiz import generate_random_integer, generate_operator, calculate_expression

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_operator(self):
        # Testing the operator generation function might involve checking if the result is one of the specified operators
        valid_operators = ['+', '-', '*']
        generated_operator = generate_operator()
        self.assertIn(generated_operator, valid_operators)

    def test_calculate_expression(self):
        test_cases = [
            (5, 2, '+', 7),
            (10, 3, '*', 30),
            # Add more test cases
        ]

        for num1, num2, operator, expected_answer in test_cases:
            result = calculate_expression(num1, num2, operator)
            self.assertEqual(result, expected_answer)

if __name__ == "__main__":
    unittest.main()
