from question_model import Question
from data import question_data

question_bank = []
for i in question_data:
    questions = Question(i['text'], i['answer'])
    question_bank.append(questions)

print(question_bank[0].text, question_bank[0].answer )