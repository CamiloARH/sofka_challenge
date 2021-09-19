from class_functions import Game, Category as ct, Questions as qu, Answers as aw, User, getint, getstr

name=input('Por favor ingresa tu nombre: ')
User.get_nameuser(name)
input('Pulse enter para continuar...')
print()
i = 1
points = 0
while i <= 5:
    category = ct.get_category(i)
    question = qu.get_question(i)
    id_question = qu.get_question_id(question)
    answers = aw.get_answer(id_question)
    answer_input = getint('Por favor digite una respuesta del 1 al 4: ')
    check = aw.get_check(id_question,answer_input)
    if check == 'True':
        print()
        print('La respuesta es correcta')
        print('Felicitaciones')
        points = ct.get_point(i, points)
        print('*'*40)
        print('')
        if i < 5:
            continue_playing = getstr('¿Quieres Continuar? S/N: ')
        else:
            break
        if continue_playing == 'n':
            break
        if continue_playing == 'no':
            break
    else:
        print('Lo siento perdiste')
        print()
        print('*'*40)
        print()
        break
    i += 1
info = User.get_save(name,points)






