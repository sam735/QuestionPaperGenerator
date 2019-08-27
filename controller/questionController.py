from paperGenerator.services.questionService import question_generator
def input_taker():
    total_marks = int(input("Enter total marks:"))
    easy_level = int(input("Enter Easy % marks:"))
    medium_level = int(input("Enter medium % marks:"))
    hard_level = int(input("Enter Hard % marks:"))
    x = question_generator(easy_level,medium_level,hard_level,total_marks)
    return x
