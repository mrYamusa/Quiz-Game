from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

quiz = []
for item in question_data:
    new_question = Question((item["text"]), (item["answer"]))
    quiz.append(new_question)

quizbrain = QuizBrain(quiz)
while quizbrain.end_of_questions():
    ans, curq = quizbrain.next_question()
    if quizbrain.is_answer_correct(ans, curq):
        pass

    if not(quizbrain.end_of_questions()):
        print("You've completed the quiz!")
        print(f"Your final score is {quizbrain.score}/{len(quizbrain.question_list)}")
