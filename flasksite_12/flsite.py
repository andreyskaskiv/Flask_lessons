"""Порядок работы с cookies"""

from flask import Flask, make_response, request

app = Flask(__name__)

menu = [{"title": "Главная", "url": "/"},
        {"title": "Добавить статью", "url": "/add_post"}]


@app.route("/")
def index():
    return "<h1>Main Page</h1>"


@app.route("/login")  # создание куков
def login():
    log = ""
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')

    res = make_response(f"<h1>Форма авторизации</h1>logged: {log}")
    res.set_cookie("logged", "yes", 30 * 24 * 3600)  # 30 * 24 * 3600 время в секундах хранения кук
    return res


@app.route("/logout")  # удаление куков
def logout():
    res = make_response("Вы больше не авторизованы!</p>")
    res.set_cookie("logged", "", 0)
    return res


if __name__ == "__main__":
    app.run(debug=True)

"""
чтобы работать с cookies через объект ответа, используется функция

set_cookie(key, value="", max_age=None)

key – название куки;
value – данные, которые сохраняются в cookies под указанным ключом;

max_age – необязательный аргумент, указывающий предельное время хранения 
данных cookies в барузере клиента (в секундах). Если время не указывается, 
то куки пропадут при закрытии браузера.
"""
