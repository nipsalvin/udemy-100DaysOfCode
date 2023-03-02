from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    questions = Question(i['text'], i['answer'])
    question_bank.append(questions)

# print(question_bank[0].text, question_bank[0].answer )
quiz = QuizBrain(question_bank)
quiz.next_question()
# print (quiz)
# while quiz.still_has_questions() == True:
while quiz.still_has_questions():
    quiz.next_question()
