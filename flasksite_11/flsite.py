"""Формирование ответа сервера, декораторы перехвата запроса"""

"""
В этом заголовке находится «служебная» информация, сообщающая браузеру, 
как интерпретировать принятые данные. Например, там указывается код ответа:

200 – все нормально;
404 – страница не найдена;
301 – выполнено перенаправление с другого URL;
401 – доступ запрещен


и так далее. Кроме того, в заголовке в параметре content-type прописывается тип данных:

text/html
text/plain
image/jpeg
audio/mp4
multipart/form-data"""

from flask import Flask, render_template

app = Flask(__name__)

menu = [{"title": "ГлавнаЯЯЯЯ", "url": "/"},
        {"title": "Добавить статью", "url": "/add_post"}]


@app.route("/")
def index():
    return render_template('index.html', menu=menu, posts=[])


if __name__ == "__main__":
    app.run(debug=True)
