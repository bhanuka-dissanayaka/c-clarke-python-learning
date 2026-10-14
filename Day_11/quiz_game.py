import random

questions = [
    {
        "question": "What is the capital of Sri Lanka?",
        "answer": "colombo"
    },
    {
        "question": "What is 5 + 5?",
        "answer": "10"
    },
    {
        "question": "Which language are we learning?",
        "answer": "python"
    },
    {
        "question": "What is 10 * 2?",
        "answer": "20"
    }
]

question_number = 0
marks = 0
random.shuffle(questions)

print("=" * 40)
print("Welcome to POP QUIZ")
print("=" * 40)


for item in questions:
    question_number += 1
    print(f"\nQuestion {question_number}")
    print(item["question"])
    user_answer = input("Your Answer : ").strip()

    if user_answer.lower() == item["answer"].lower():
        print("Correct! Moving to next question")
        marks += 10

    else:
        print("Wrong Answer! Game Over")
        break

print(f"\n====================================="
      f"\nYour Final Marks : {marks}"
      f"\n=====================================")



