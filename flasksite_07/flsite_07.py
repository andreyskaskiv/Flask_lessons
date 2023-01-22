"""Декоратор errorhandler, функции redirect и abort"""

"""
Следующим важным моментом при разработке сайта является 
отлавливание некоторых ошибок ответа сервера. Например, 
при отсутствии какой-либо страницы пользователь в 
браузере. 
Чтобы создать такой обработчик, следует использовать 
специальный декоратор errorhandler с указанием в нем 
кода ответа, с которым будет ассоциирована функция представления:
"""

from flask import (Flask,
                   render_template,
                   url_for,
                   request,
                   flash,
                   session,
                   redirect,
                   abort)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="О сайте", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
        print(request.__dict__)
        print(request.form)
        print(request.form['username'])
    return render_template('contact.html', title="Обратная связь", menu=menu)


"""
Request redirect (Перенаправление запроса) 
"""


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "Andrey" and request.form['password'] == "123456789":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)


"""
Смотрите, если в сессии нет ключа 'userLogged', то вызывается функция abort, которая 
указывает серверу вернуть код ошибки 401. Иначе, отображается профайл пользователя.

Таким образом, пользователь может смотреть только свой профайл и даже если попытается 
в запросе браузера указать логин другого человека, то получит ошибку доступа.
"""


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Пользователь: {username}"


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404


if __name__ == "__main__":
    app.run(debug=True)
