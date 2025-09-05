def quiz_game():
    # Step 1: Questions & Answers
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["1. Delhi", "2. Mumbai", "3. Kolkata", "4. Chennai"],
            "answer": "1"
        },
        {
            "question": "Which programming language is known as the 'mother of all languages'?",
            "options": ["1. Python", "2. C", "3. Java", "4. Pascal"],
            "answer": "2"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["1. 10", "2. 11", "3. 12", "4. 13"],
            "answer": "3"
        },
        {
            "question": "Who is known as the Father of Computers?",
            "options": ["1. Charles Babbage", "2. Alan Turing", "3. John von Neumann", "4. Bill Gates"],
            "answer": "1"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"],
            "answer": "2"
        },
        {
            "question": "What is the national animal of India?",
            "options": ["1. Lion", "2. Tiger", "3. Elephant", "4. Peacock"],
            "answer": "2"
        },
        {
            "question": "Which is the smallest prime number?",
            "options": ["1. 5", "2. 3", "3. 1", "4. 2"],
            "answer": "4"
        },
        {
            "question": "In Python, which keyword is used to define a function?",
            "options": ["1. func", "2. def", "3. function", "4. lambda"],
            "answer": "2"
        }
    ]

    score = 0  # Step 4: Track score

    # Step 2 & 3: Ask and check
    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        user_answer = input("Enter the option number: ")

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer is option", q["answer"])

    # Step 5: Final score
    print("\nQuiz Over! Your score is:", score, "/", len(questions))

# Run the game
quiz_game()
