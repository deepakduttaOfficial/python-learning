from question_model import Questions
from data import question_data
import data
from quiz_brain import QuizBrain


question_bank = []
for data in question_data:
    question_bank.append(Questions(data["question"], data["correct_answer"]))

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You have completed the quiz")
print(f"You final score was {quiz_brain.score}/{quiz_brain.question_number}")