import random

# Dictionary of questions, answers, and difficulty levels
quiz_questions = {
    "Formula 1 Racing": [
        {
            "question": "Which team holds the record for winning the most Constructors' Championships in the history of Formula 1?",
            "options": ["A) Mercedes", "B) Williams", "C) MC Laren", "D) Ferrari"],
            "correct_answer": "D"
        },
        {
            "question": "Who is the only driver to have won a Formula 1 Grand Prix in a car bearing his own name?",
            "options": ["A) Bruce McLaren", "B) Enzo Ferrari", "C) Niki Lauda", "D) Frank Williams"],
            "correct_answer": "A"
        },
        {
            "question": "Which Formula One driver has had the most podium finishes?",
            "options": ["A) Fernando Alonso", "B) Michael Schumacher", "C) Alain Prost", "D) Ayrton Senna"],
            "correct_answer": "B"
        }
    ],
    "Cricket": [
        {
            "question": " How many times has India won the Cricket World Cup??",
            "options": ["A) 4", "B) 3", "C) 2", "D) 1"],
            "correct_answer": "B"
        },
        {
            "question": "When did India play its first Test match??",
            "options": ["A) 1931", "B) 1930", "C) 1932", "D) 1929"],
            "correct_answer": "C"
        },
        {
            "question": "What is the moniker given to the Indian cricket team??",
            "options": ["A) The Team of Lions", "B) The Indian Army", "C) Men In Blue", "D) None "],
            "correct_answer": "C"
        }
    ]
}

def quiz_game():
    print("Welcome to the Quiz Game!")
    print("Choose a topic:")
    
    # Print available topics
    topics = list(quiz_questions.keys())
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    # Select topic
    while True:
        try:
            choice = int(input("Enter your choice (1-" + str(len(topics)) + "): "))
            if 1 <= choice <= len(topics):
                chosen_topic = topics[choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(topics))
        except ValueError:
            print("Invalid choice. Please enter a number.")

    print(f"You've chosen {chosen_topic}.")

    # Select difficulty level
    difficulty_levels = ["Easy", "Medium", "Hard"]
    while True:
        print("Choose difficulty level:")
        for i, level in enumerate(difficulty_levels):
            print(f"{i+1}. {level}")
        
        try:
            difficulty_choice = int(input("Enter your choice (1-3): "))
            if 1 <= difficulty_choice <= 3:
                chosen_difficulty = difficulty_levels[difficulty_choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

    print(f"You've chosen {chosen_difficulty} difficulty level.")
    print("Let's start the quiz!")

    # Initialize score
    score = 0

    # Shuffle questions for variety
    random.shuffle(quiz_questions[chosen_topic])

    # Iterate over questions
    for question_data in quiz_questions[chosen_topic]:
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["correct_answer"]

        print("\n" + question)
        for option in options:
            print(option)

        # Get user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

        # Validate answer
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", correct_answer)

    # Display final score
    print("\nQuiz completed!")
    print("Your final score is:", score, "out of", len(quiz_questions[chosen_topic]))

# Run the quiz game
quiz_game()
