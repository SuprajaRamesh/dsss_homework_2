import random

def generate_random_number(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def select_random_math_operator():
    """
    Random math operator selection.
    """
    return random.choice(['+', '-', '*'])


def perform_math_operation(num1, num2, operator):
    """
    Perform given math operation on 2 numbers.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+': answer = num1 + num2
    elif operator == '-': answer = num1 - num2
    else: answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # get all values for the problem
        num1 = generate_random_number(1, 10); num2 = generate_random_number(1, 5)
        operator = select_random_math_operator()

        # get correct solution
        problem, answer = perform_math_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # get user input
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except:
            print(f"Invalid answer. The correct answer is {answer}.")
            continue

        # validate user answer
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
