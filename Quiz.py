#Simple quiz
import random
questions = [
    {
        "question": "What is 7 * 8?",
        "options": ["a) 67", "b) 45", "c) 56", "d) 87"],
        "answer": "c"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["a) Mitochondria", "b) The cell itself", "c) Nucleus", "d) Cytoplasm"],
        "answer": "a"
    },
    {
        "question": "What color is the sky on a clear day?",
        "options": ["a) Green", "b) Red", "c) Blue", "d) Gray"],
        "answer": "c"
    },
    {
        "question": "What is the capital of Romania?",
        "options": ["a) Berlin", "b) Rome", "c) Sarajevo", "d) Bucharest"],
        "answer": "d"
    },
    {
        "question": "What symbol is used to start a comment in Python?",
        "options": ["a) //", "b) <!--", "c) #", "d) **"],
        "answer": "c"
    }
]





def start_quiz():
    score = 0
    random.shuffle(questions)
    for i in questions:
        print("\n" + i["question"])
        for option in i["options"]:
            print(option)
        user_answer = input("Your answer (a/b/c/d): ").strip().lower()
        while user_answer not in ["a", "b", "c", "d"]:
            print("Enter a valid option (a, b, c, d)!")
            user_answer = input("Your answer (a/b/c/d): ").strip().lower()
        if user_answer == i["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            print(f"You're wrong! The correct answer was {i['answer']}.")
    print("\nYour quiz is finished!")
    print(f"Your final score is {score}/{len(questions)}")
while True:
    start_quiz()
    again = input("\nPlay again? (y/n): ").lower().strip()
    if again != "y":
        print("Thanks for playing!")
        break