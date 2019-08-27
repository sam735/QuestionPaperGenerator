def print_question_paper(quetions):
    print('Difficulty label-------------------->Easy')
    print(' ')
    #import pdb;pdb.set_trace()
    for quetion in quetions:
        if quetion['difficulty'] == 'Easy':
            print(quetion['text'],'                      marks:',quetion['marks'])
    
    print(' ')
    print('Difficulty label-------------------->Medium')
    print(' ')
    for quetion in quetions:
        if quetion['difficulty'] == 'Medium':
            print(quetion['text'],'                      marks:',quetion['marks'])
    
    print(' ')
    print('Difficulty label--------------------->Hard')
    print(' ')
    for quetion in quetions:
        if quetion['difficulty'] == 'Hard':
            print(quetion['text'],'                      marks:',quetion['marks'])