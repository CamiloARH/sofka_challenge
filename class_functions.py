import sqlite3
import random

db = sqlite3.connect("sofka_challenge.sqlite")


class Game(object):

    def __init__(self, name='User', level=1, points=0, question='', answer=''):
        self._name = name
        self.level = level
        self.points = points
        self.question = question
        self.answer = answer

class Category(Game):
    
    def __init__(self):
        super(Category, self).__init__(level=1, points=0)

    def get_category(lv=1):
        cursor = db.execute("SELECT Category_name FROM Category WHERE (Level=?)", (lv, ))
        category_level = cursor.fetchone()
        print('Estás en la', category_level[0])
        return category_level

    def get_point(lv=1, point=0):
        cursor = db.execute("SELECT Points FROM Category WHERE (Level=?)", (lv, )).fetchone()
        point = point + cursor[0]
        print('Ganaste', cursor[0], 'puntos.')
        print()
        print(f'Tus puntos actuales son:  {point}.')
        return point


class Questions(Game):
    def __init__(self):
        super(Questions, self).__init__(question='')

    def get_question(lv):
        random_number= random.randrange(0, 5)
        # print(random_number)  # TODO
        questions = db.execute("SELECT Question FROM Questions WHERE (Category_id=?)", (lv, )).fetchall()
        print('tu pregunta es:', questions[random_number][0])
        return questions[random_number][0]

    def get_question_id(questions):
        question_id = db.execute("SELECT Id FROM Questions WHERE (Question=?)", (questions, )).fetchone()
        # print(question_id[0])  # TODO
        return question_id[0]


class Answers(Game):
    def __init__(self):
        super(Answers, self).__init__(answer='')

    def get_answer(question_id):
        for answer in enumerate(db.execute("SELECT Answer FROM Answers WHERE (Question_id=?)", (question_id, )).fetchall()):
            print(answer[0] + 1, ':', answer[1][0])

    def get_check(question_id, answer_input):
        check = db.execute("SELECT Correct FROM Answers WHERE (Question_id=?)", (question_id, )).fetchall()
        return check[answer_input-1][0]


class User(Game):

    def __init__(self):
        super().__init__(name='User')

    def get_nameuser(name):
        print('Hola',name,'bienvenido a este pequeño juego de preguntas')
        print('Mucha suerte')

    def get_save(name, points):

        db.execute("INSERT INTO Users VALUES (?, ?)", (name, points))
        print()
        save = db.execute("SELECT * FROM Users").fetchall()[0]
        print(save[0], ', tu puntuación total fue:', save[1])


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 5:
                return number
            else:
                print('No es un numero valido, trata de nuevo')
        except ValueError:
            print("Numero invalido, por favor trate de nuevo")


def getstr(prompt):
    while True:
        try:
            answer_str = input(prompt).casefold()
            if answer_str == 's' or answer_str == 'si':
                print('Perfecto')
                print('*'*40)
                print()
                return answer_str
            if answer_str == 'n' or answer_str == 'no':
                print('Gracias por jugar')
                print('Esperamos verte pronto')
                print()
                print('*'*40)
                print()
                return answer_str
            else:
                print('Trata de nuevo')
        except TypeError:
            print("Numero no son validos, por favor trate de nuevo")



# qi = Questions.get_question(1)
# qid= Questions.get_question_id(qi)
# answ =Answers.get_answer(qid)
# answ_inpu = 1
# check = Answers.get_check(qid,answ_inpu)
