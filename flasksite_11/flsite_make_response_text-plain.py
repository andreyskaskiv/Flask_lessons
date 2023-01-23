"""Формирование ответа сервера, декораторы перехвата запроса"""

from flask import Flask, render_template, make_response

app = Flask(__name__)

menu = [{"title": "Главна make_response", "url": "/"},
        {"title": "Добавить статью", "url": "/add_post"}]


# @app.route("/")
# def index():
#     return render_template('index.html', menu=menu, posts=[])


@app.route("/")
def index():
    content = render_template('index.html', menu=menu, posts=[])
    res = make_response(content)
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'flasksite'
    return res


"""
Здесь:
res_body – передаваемое содержимое (контент);
status_code – код ответа сервера (по умолчанию 200).
"""

if __name__ == "__main__":
    app.run(debug=True)
