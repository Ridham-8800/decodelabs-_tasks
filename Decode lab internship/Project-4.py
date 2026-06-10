# General Knowledge Quiz

score = 0

# Question 1
answer = input("1. What is the capital of France? ")

if answer.lower() == "paris":
    score += 1
    print("Correct!")
else:
    print("Wrong! The answer is Paris.")

# Question 2
answer = input("\n2. Which planet is known as the Red Planet? ")

if answer.lower() == "mars":
    score += 1
    print("Correct!")
else:
    print("Wrong! The answer is Mars.")

# Question 3
answer = input("\n3. How many days are there in a week? ")

if answer == "7":
    score += 1
    print("Correct!")
else:
    print("Wrong! The answer is 7.")

# Final Score
print("\nQuiz Finished!")
print("Your Final Score:", score, "/ 3")