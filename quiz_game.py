import random

def load_quiz_questions():
    questions = [
        {
            'question': 'Which avenger is green in color?',
            'choices': ['Ant Man', 'Thor', 'Captain America', 'Hulk'],
            'correct_answer': 'Hulk'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'choices': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
            'correct_answer': 'Mars'
        },
        {
            'question': 'What is the largest mammal in the world?',
            'choices': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 'Blue Whale'
        }
        
    ]
    return questions

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions to test your knowledge.")

def present_quiz_questions(questions):
    score = 0
    for index, question in enumerate(questions, 1):
        print(f"\nQuestion {index}: {question['question']}")
        for i, choice in enumerate(question['choices'], 1):
            print(f"{i}. {choice}")
        
        user_answer = input("Your answer: ")
        if user_answer.lower() == question['correct_answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {question['correct_answer']}")
    
    return score

def display_final_results(score, total_questions):
    print(f"\nYour final score is: {score}/{total_questions}")
    if score == total_questions:
        print("Congratulations! You got all the questions right.")
    elif score >= total_questions / 2:
        print("Good job! You did well.")
    else:
        print("Keep studying. You can do better next time.")

def play_quiz_game():
    questions = load_quiz_questions()
    total_questions = len(questions)
    display_welcome_message()
    
    while True:
        score = present_quiz_questions(questions)
        display_final_results(score, total_questions)
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_quiz_game()
