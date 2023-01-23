"""Формирование ответа сервера, декораторы перехвата запроса"""

from flask import Flask, make_response

app = Flask(__name__)

menu = [{"title": "Главна make_response", "url": "/"},
        {"title": "Добавить статью", "url": "/add_post"}]


# @app.route("/")
# def index():
#     return render_template('index.html', menu=menu, posts=[])


# @app.route("/")
# def index():
#     content = render_template('index.html', menu=menu, posts=[])
#     res = make_response(content)
#     res.headers['Content-Type'] = 'text/plain'
#     res.headers['Server'] = 'flasksite'
#     return res


# @app.route("/")
# def index():
#     img = None
#     with app.open_resource(app.root_path + "/static/images/ava.png", mode="rb") as f:
#         img = f.read()
#
#     if img is None:
#         return "None image"
#
#     res = make_response(img)
#     res.headers['Content-Type'] = 'image/png'
#     return res


@app.route("/")
def index():
    res = make_response("<h1>Ошибка сервера</h1>", 500)
    return res


"""
Последний способ создать ответ – использовать кортежи в одном из следующих форматов:
(response, status, headers)
(response, headers)
(response, status)
response — строка, представляющая собой тело ответа, status — код состояния HTTP, 
который может быть указан в виде целого числа или строки, а headers — словарь со 
значениями заголовков. Например, так:
"""


@app.errorhandler(404)
def pageNot(error):
    return ("Страница не найдена", 404)


if __name__ == "__main__":
    app.run(debug=True)
