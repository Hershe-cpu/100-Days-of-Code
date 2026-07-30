from data import Data

class QuizBrain:
    def __init__(self, q_list):
        self.question = q_list
        self.question_number = 0
        self.score = 0


    def still_has_question(self):
        return self.question_number < len(self.question)

    def next_question(self):
        current_quest = self.question[self.question_number]
        user_ans = input(f"Q.{self.question_number+1}: {current_quest['question']} (True/False)?: ")
        wow = self.check_answer(user_ans)
        self.question_number += 1
        return wow


    def check_answer(self, user_ans):
        current_quest = self.question[self.question_number]
        if user_ans.capitalize() == current_quest["correct_answer"]:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was:  {current_quest['correct_answer']}")
            print(f"Your current score is:  {self.score}/{self.question_number+1}")
            return True
        else:
            print("That's wrong.!")
            print(f"The correct answer was:  {current_quest['correct_answer']}")
            print(f"Your current score is:  {self.score}/{self.question_number+1}")
            return False

quiz= QuizBrain(Data)

while quiz.still_has_question():
    guess_ans = quiz.next_question()
    print("\n")

print(f"Quiz finished ")
print(f"Your final score is:  {quiz.score}/{quiz.question_number}")



