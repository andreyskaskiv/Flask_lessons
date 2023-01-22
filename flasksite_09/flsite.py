"""Добавление и отображение статей из БД"""

import os
import sqlite3

from flask import (Flask,
                   render_template,
                   g,
                   request,
                   flash,
                   abort)

from flasksite_09.FDataBase import FDataBase

# конфигурация
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def connect_db():
    """Создадим общую функцию для установления соединения с БД"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


"""
create_db()
Здесь мы используем метод open_resource, который открывает файл 'sq_db.sql' на чтение, 
расположенный в рабочем каталоге нашего приложения. Затем, для открытой БД выполняется скрипт, 
записанный в файле 'sq_db.sql'. В конце вызывается метод commit, чтобы изменения применились 
к текущей БД, и метод close закрывает установленное соединение.
"""


def get_db():
    """Соединение с БД, если оно еще не установлено"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


"""
get_db()
Смотрите, мы здесь используем объект g контекста приложения, которое создается в момент поступления запроса. 
В этом объекте можно сохранять любую пользовательскую информацию, которая будет доступна в любой функции и шаблонах, 
в пределах этого запроса. Причем, для разных запросов, объект g будет разным, то есть, он уникален в пределах 
текущего запроса.

Далее, мы проверяем: было ли соединение уже установлено (существует ли атрибут link_db, который мы создаем 
в момент соединения с БД. Если соединения еще нет, то устанавливаем его и, затем, возвращаем. Как вы уже догадались, 
если где-либо в функциях (или шаблонах) будет повторное обращение к этой функции, то она просто возвратит ранее 
установленное соединение, что очень удобно.
"""


@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с БД, если оно было установлено"""
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/")
def index():
    db = get_db()  # Момент поступления в db запроса мы можем «поймать» непосредственно в обработчике.
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.getMenu(), posts=dbase.getPostsAnonce())


"""ДОБАВЛЕНИЕ_СТАТЬИ"""


@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')

    return render_template('add_post.html', menu=dbase.getMenu(), title="Добавление статьи")


"""
addPost()
Вначале идет подключение к БД, и после этого проверка: если были переданы данные от формы методом POST, 
то нужно осуществить добавление статьи в таблицу posts. Для этого вначале проверяем наличие данных в 
полях name и post и, если все нормально, то вызываем метод addPost класса FDataBase (позже мы его пропишем).
"""

"""ОТОБРАЖЕНИЕ_СТАТЬИ"""


@app.route("/post/<int:id_post>")
def showPost(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.getPost(id_post)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


"""
С его помощью будут отображаться статьи с указанным id_post. Вначале также устанавливается 
соединение с БД, затем, вызывается метод getPost класса FDataBase, который возвращает заголовок 
статьи и ее текст, а, иначе, при ошибке считывания данных из таблицы posts, формируется ответ 
сервера 404 – страница не найдена. 
"""

"""ОТОБРАЖЕНИЕ_СПИСКА_СТАТЕЙ"""

if __name__ == "__main__":
    app.run(debug=True)
