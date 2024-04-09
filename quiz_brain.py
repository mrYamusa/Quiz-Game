class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    # TODO ask question
    def next_question(self):
        """Generates questions from the question bank (data.py)"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text}? (True/False)").title()
        return user_ans, current_question

    def is_answer_correct(self, usrans, curq):
        """Checks if answer is correct and increments user score"""
        if usrans == curq.answer:
            self.score += 1
            print(f"You got it right!\n the correct answer is {curq.answer}")
            print(f" Your score is {self.score}/{self.question_number}")
            return True
        else:
            print("Your answer is wrong. You lose!")
            return False

    def end_of_questions(self):
        """If questions are exhausted then return false"""
        return self.question_number < len(self.question_list)