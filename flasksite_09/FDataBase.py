import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения из БД")
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False

        return True

    def getPost(self, postId):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE id = {postId} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return (False, False)

    def getPostsAnonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return []


"""
getMenu(self)
Смотрите, я здесь для удобства создал вспомогательный класс FDataBase, который запоминает 
ссылку на БД и, затем, с помощью метода getMenu возвращает список для отображения 
меню в шаблоне index.html. 

Здесь в конструкторе запоминается ссылка на БД и ссылка на класс курсор, через который 
осуществляется взаимодействие с таблицами этой БД. Далее, идет метод getMenu и в 
блоке try/except осуществляется выборка всех записей из таблицы mainmenu. 
Если операция прошла успешно, то возвращается список словарей из записей, а иначе – пустой список.


addPost(self, title, text)
Здесь нам нужно добавить метод addPost в класс FDataBase:
Ему передаются два аргумента: title и text. Затем, вычисляется текущее время добавления 
статьи (в секундах) и выполняется запрос на добавление переданных данных. 
После этого обязательно нужно вызвать метод commit для физического сохранения изменений в БД.

При нажатии на кнопку «Добавить» данные будут переданы обработчику /add_post и при успешной 
проверке принятых значений, статья будет помещена в таблицу posts.


getPost(self, postId)
Здесь все вполне очевидно. Сначала выбираются поля title и text для статьи, у которой id равен posted. 
Если метод fetchone возвращает не None, то есть, статья была найдена в БД, то возвращается кортеж из ее 
названия и текста. Иначе, возвращается кортеж из значений False.


getPostsAnonce(self)
Мы здесь выбираем все записи из таблицы posts и сортируем их по новизне: сначала самые свежие, затем, 
более позние. После этого выбираем все записи с помощью метода fetchall и при успешности этой операции, 
возвращаем список. Иначе, возвращается пустой список.

"""
