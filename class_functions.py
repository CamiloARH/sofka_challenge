import sqlite3
import random

db = sqlite3.connect("sofka_challenge.sqlite")

# Main Class
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

    # To get the category
    def get_category(lv=1):
        cursor = db.execute("SELECT Category_name FROM Category WHERE (Level=?)", (lv, ))
        category_level = cursor.fetchone()
        print('Estás en la', category_level[0])
        return category_level

    # To get the points
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

    # To get the Question to ask
    def get_question(lv):
        random_number= random.randrange(0, 5)
        questions = db.execute("SELECT Question FROM Questions WHERE (Category_id=?)", (lv, )).fetchall()
        print('tu pregunta es:', questions[random_number][0])
        return questions[random_number][0]

    # To get the Id Question
    def get_question_id(questions):
        question_id = db.execute("SELECT Id FROM Questions WHERE (Question=?)", (questions, )).fetchone()
        return question_id[0]


class Answers(Game):
    def __init__(self):
        super(Answers, self).__init__(answer='')

    # To get the correct Answer of the question
    def get_answer(question_id):
        for answer in enumerate(db.execute("SELECT Answer FROM Answers WHERE (Question_id=?)", (question_id, )).fetchall()):
            print(answer[0] + 1, ':', answer[1][0])

    # To check if the answer was right
    def get_check(question_id, answer_input):
        check = db.execute("SELECT Correct FROM Answers WHERE (Question_id=?)", (question_id, )).fetchall()
        return check[answer_input-1][0]


class User(Game):

    def __init__(self):
        super().__init__(name='User')

    # Said hi to the User
    def get_nameuser(name):
        print('Hola',name,'bienvenido a este pequeño juego de preguntas')
        print('Mucha suerte')

    # To get the user information save
    def get_save(name, points):

        db.execute("INSERT INTO Users VALUES (?, ?)", (name, points))
        print()
        save = db.execute("SELECT * FROM Users").fetchall()[0]
        print(save[0], ', tu puntuación total fue:', save[1])


# Loop for numbers: INT
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


# Loop for si o no: STR
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


