from paperGenerator.Inmemory.inMemoryDb import question_store

def question_generator(easy, medium, hard, marks):
    easy_marks = (marks * easy)/100
    medium_marks = (marks * medium)/100
    hard_marks = (marks * hard)/100
    easy_quetions = question_store.get('Easy')
    medium_quetions = question_store.get('Medium')
    hard_quetions = question_store.get('Hard')
    questions = []
    sum = 0
    i = 0
    for easy in easy_quetions:
        sum = sum + easy.get('marks')
        if sum <= easy_marks :
            questions.append(easy)
        else:
            sum = sum - easy.get('marks')
            break
    
    if sum != easy_marks:
        remaning_marks = easy_marks-sum
        for j in range(i-1,len(easy_quetions),1):
            if easy_quetions[j].get('marks') == remaning_marks:
                questions.append(easy_quetions[j])
                break
        # questions.append({
        #                     'text':'some question',
        #                     'subject':'xyz',
        #                     'topic':'pqrs',
        #                     'difficulty':'Easy',
        #                     'marks':remaning_marks
        #                 })
    sum = 0
    i = 0
    for medium in medium_quetions:
        i += 1
        sum = sum + medium.get('marks')
        if sum <= medium_marks:
            questions.append(medium)
        else:
            sum = sum -medium.get('marks')
            break
    
    if sum != medium_marks:
        remaning_marks = medium_marks-sum
        for j in range(i-1,len(medium_quetions),1):
            if medium_quetions[j].get('marks') == remaning_marks:
                questions.append(medium_quetions[j])
                break
        # questions.append({
        #                     'text':'some question',
        #                     'subject':'xyz',
        #                     'topic':'pqrs',
        #                     'difficulty':'Medium',
        #                     'marks':remaning_marks
        #                 })
    sum = 0
    i = 0
    for hard in hard_quetions:
        sum = sum + hard.get('marks')
        if sum <= hard_marks:
            questions.append(hard)
        else:
            sum = sum -hard.get('marks')
            break
    
    if sum != hard_marks:
        remaning_marks = hard_marks-sum
        for j in range(i-1,len(hard_quetions),1):
            if hard_quetions[j].get('marks') == remaning_marks:
                questions.append(hard_quetions[j])
                break
        # questions.append({
        #                     'text':'some question',
        #                     'subject':'xyz',
        #                     'topic':'pqrs',
        #                     'difficulty':'Hard',
        #                     'marks':remaning_marks
        #                 })
    return questions
