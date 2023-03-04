class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list

    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        input (f'Q{self.q_num}: {current_question.text} (True / False): \n')
    
    def still_has_questions(self):
        # if self.q_num < len(self.q_list):
        #     return True
        # else:
        #     return False
        # Shorter method is
        return self.q_num < len(self.q_list)

