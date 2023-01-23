"""Формирование ответа сервера, декораторы перехвата запроса"""

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

menu = [{"title": "Главна Interception of requests", "url": "/"},
        {"title": "Добавить статью", "url": "/add_post"}]

"""
before_first_request – выполняет функцию до обработки первого запроса;
before_request – выполняет функцию до обработки текущего запроса;
after_request – выполняет функцию после обработки запроса (такая функция не 
вызывается при возникновении исключений в обработчике запросов);
teardown_request (похож на after_request) – вызванная функция всегда будет 
выполняться вне зависимости от того, возвращает ли обработчик исключение (ошибку) или нет.
"""


@app.route("/")
def index():
    return render_template('index.html', menu=menu, posts=[])


@app.before_first_request
def before_first_request():
    print("before_first_request() called")


@app.before_request
def before_request():
    print("before_request() called")


@app.after_request
def after_request(response):
    print("after_request() called")
    return response


@app.teardown_request
def teardown_request(response):
    print("teardown_request() called")
    return response


if __name__ == "__main__":
    app.run(debug=True)
