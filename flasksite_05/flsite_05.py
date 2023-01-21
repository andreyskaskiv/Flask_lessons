"""Подключение внешних ресурсов и работа с формами"""

"""
HTML с нуля: урок 8 - каскадные таблицы стилей, начало
https://www.youtube.com/watch?v=CkTJXpS7KS4&list=PLA0M1Bcd0w8wRiyGX_9y-fUiBPi1vqaTb&index=10
"""


"""
https://github.com/selfedu-rus/flasksite-17
"""


from flask import (Flask,
                   render_template,
                   url_for,
                   request)

app = Flask(__name__)

"""
Далее, добавим ссылки нашим пунктам меню:
<li><a href="{{m.url}}">{{m.name}}</a></li>
А само меню в программе представим в виде списка словарей:
"""
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


"""
Дело в том, что в обработчике мы должны явно указать: 
может ли он принимать данные методом POST. 
Для этого нужно прописать параметр methods со значением POST и GET запросы
как элемент списка:
"""
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        print(request.form)
        print(request.form['username'])
    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


if __name__ == "__main__":
    app.run(debug=True)
