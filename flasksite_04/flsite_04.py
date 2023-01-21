"""Функция url_for и переменные URL-адреса"""
"""url_for() - она позволяет генерировать URL-адрес по имени функции-обработчика."""

from flask import (Flask,
                   render_template,
                   url_for)

app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]


@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="О сайте", menu=menu)


"""
url_for - с обычными путями и динамическими
@app.route("/url/<variable>")

@app.route("/profile/<int:username>")

int – должны присутствовать только цифры;
float – можно записывать число с плавающей точкой;
path – можно использовать любые допустимые символы URL плюс символ слеша ‘/’.
"""


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username="selfedu"))

if __name__ == "__main__":
    app.run(debug=True)
