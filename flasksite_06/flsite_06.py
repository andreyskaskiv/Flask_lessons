"""Мгновенные сообщения - flash, get_flashed_messages"""

"""
Этот функционал встроен во фреймворк Flask и реализуется с помощью двух функций:

flash() – формирование сообщения пользователю;
get_flashed_messages() – обработка сформированных сообщений в шаблоне документа.
Их синтаксис, следующий:

flask.flash(message, category=’message’)

flask.get_flashed_messages(with_categories=False, category_filter=[])

message – текст сообщения;
category – категория сообщения;
with_categories – разрешает использование категорий при извлечении сообщений;
category_filter – список разрешенных категорий при выборке сообщений.
"""

from flask import (Flask,
                   render_template,
                   url_for,
                   request,
                   flash)

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


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


if __name__ == "__main__":
    app.run(debug=True)
