question = {
    "what is the captial of India?" :"New Dehli",
    "Which planet is know as the red planet? " : "Mars",
    "what language is this ?": "Python",
    "Who created the Python programming language?": "Guido van Rossum",
    " Which keyword is used to define a function in Python?": "def"
}
def ask_question(question , answer):
    user = input(f"{question}").strip().lower()
    return user == answer
score = 0
for q, a in questions.items():
    if ask_question(q, a):
        print("Correct!")
        score += 1
    else:
        print(f"Nope! The answer was {a}")
