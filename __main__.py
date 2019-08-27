from paperGenerator.controller.questionController import input_taker
from paperGenerator.util import print_question_paper

if __name__ == "__main__":
    quetions = input_taker()
    print_question_paper(quetions)