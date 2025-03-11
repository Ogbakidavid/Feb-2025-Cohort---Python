# ============ Greeting App ==========
name = input("What is your name: ")
color = input("What is your favorite color: ")

print(f"Hello, {name}! Your favorite color, {color}, is awesome ")

# =========== Quiz Game ==============
import random

def quiz():
    questions = [
        {
            "questions": "What is the capital of Ethiopia",
            "options": ["A). Accra", "B). Asmara", "C). Addis Ababa", "D). Algiers"],
            "answer": "C"
        },
        {
            "questions": "What actor played the role sliver surfer in the movie fantastic four",
            "options": ["A). Laurence Fishburne", "B). Joseph Quinn", "C). Jack Sparrow", "D). Pedro Pascal"],
            "answer": "A"
        },
        {
            "questions": "What is the scientific name for the python snake",
            "options": ["A). Python regius", "B). Python molurus", "C). Pythonidae serpertis", "D). Python vulgaris"],
            "answer": "B"
        }
    ]

    score = 0
    for q in questions:
        print("\n" + q["questions"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").strip().upper()
        if answer == q["answer"]:
            score += 1
            print("Correct!")
        else: 
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nYour final score is {score}/{len(questions)} 🏆")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        quiz()
    else:
        print("Thanks for playing: 🎉")

if __name__ == "__main__":
    quiz()


