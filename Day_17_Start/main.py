from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for questions in question_data:
    question = questions['text']
    answer = questions['answer']
    new_question = Question(question, answer)
    question_bank.append(new_question)
print(question_bank)
quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz.")






