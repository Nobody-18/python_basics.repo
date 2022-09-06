class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompt = ["""bWhat color are apples\n a.red b.purple c.yellow\n\n"""
, """What color are bananas \n a.teel b.yelllow c.orange\n\n"""
, """What color are oranges\n a.red b.orange c.blue\n
"""]
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "b")

]


def run_test(question):
    score = 0
    for question in question:
        if input(question.prompt) == question.answer:
            score += 1
    print("you got "+str(score)+"/3 answers correct")


run_test(questions)
