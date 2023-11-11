import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within the given range.
    """
    return random.randint(min_value, max_value)


def generate_operator():
    """
    Generates a random arithmetic operator: +, -, or *.
    """
    return random.choice(['+', '-', '*'])


def calculate_expression(num1, num2, operator):
    """
    Calculates the result of the expression based on the operator.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # Changed 5.5 to 5 for integer operations
        operator = generate_operator()

        problem = f"{num1} {operator} {num2}"
        correct_answer = calculate_expression(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Please enter a valid integer for the answer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
