"""Порядок работы с сессиями (session)"""
import datetime

from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '026dcb1fbc52810fb87cdf40cd832e07361e9f8b'
app.permanent_session_lifetime = datetime.timedelta(
    days=10)  # Теперь сессии будут максимум храниться 10 дней в браузере клиента.


@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # обновление данных сессии
    else:
        session['visits'] = 1  # запись данных в сессию

    print(f"Число просмотров: {session['visits']}")
    return f"<h1>Main Page</h1>Число просмотров: {session['visits']}"


data = [1, 2, 3, 4]


@app.route("/session")
def session_data():
    session.permanent = True  # явно указать время жизни сессий в куках которое по умолчанию составляет 31 день. app.permanent_session_lifetime
    if 'data' not in session:
        session['data'] = data
    else:
        session['data'][1] += 1
        session.modified = True  # Этим мы явно указываем Flask, что состояние сессии изменилось и ее нужно обновить в браузере.

    print(f"session['data']: {session['data']}")
    return f"session['data']: {session['data']}"


if __name__ == "__main__":
    app.run(debug=True)

"""
Для надежности этот ключ должен содержать самые 
разные символы и один из хороших способов его 
сгенерировать – это воспользоваться следующей 
командой пакета os:

import os
os.urandom(20).hex()
"""
