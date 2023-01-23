"""Формирование ответа сервера, декораторы перехвата запроса"""

from flask import Flask, redirect, url_for

app = Flask(__name__)

menu = [{"title": "Главна make_response", "url": "/"},
        {"title": "Добавить статью", "url": "/add_post"}]


@app.route("/")
def index():
    return "<h1>Main Page</h1>", 200, {'Content-Type': 'text/plain'}


@app.errorhandler(404)
def pageNot(error):
    return ("Страница не найдена", 404)


@app.route('/transfer')
def transfer():
    return redirect(url_for('index'), 301)


""". Это делается с помощью перенаправления с кодами:

301 – страница перемещена на другой постоянный URL-адрес;
302 – страница перемещена временно на другой URL-адрес.
Чтобы во Flask выполнить перенаправление с прежнего URL на новый, можно использовать функцию

redirect(location, status)

о которой мы уже говорили. """

if __name__ == "__main__":
    app.run(debug=True)
