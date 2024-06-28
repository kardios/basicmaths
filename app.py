import streamlit as st
import random

def generate_question(difficulty):
    if difficulty == 'easy':
        range_min, range_max = 1, 20
        num_questions = 5
    elif difficulty == 'medium':
        range_min, range_max = 1, 50
        num_questions = 7
    elif difficulty == 'hard':
        range_min, range_max = 1, 100
        num_questions = 10
    else:
        raise ValueError("Invalid difficulty level")

    questions = []
    for _ in range(num_questions):
        operation = random.choice(['+', '-'])
        if operation == '+':
            while True:
                a = random.randint(range_min, range_max)
                b = random.randint(range_min, range_max)
                if a + b <= 100:
                    break
            question = f"{a} + {b}"
        else:
            while True:
                a = random.randint(range_min, range_max)
                b = random.randint(range_min, a)  # Ensures a - b is non-negative
                if a - b <= 100:
                    break
            question = f"{a} - {b}"

        questions.append(question)

    return questions

# Example usage:
difficulty_level = 'medium'  # 'easy', 'medium', or 'hard'
questions = generate_question(difficulty_level)
for question in questions:
    st.header(question)
