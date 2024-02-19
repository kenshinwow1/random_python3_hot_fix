from flask import Flask, render_template, request

import random

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 3
    message = ''
    
    for _ in range(attempts):
        guess = int(request.form['guess'])
        if guess == secret_number:
            message = 'Поздравляем! Вы угадали число!'
            break
        elif guess < secret_number:
            message = 'Попробуйте число больше.'
        else:
            message = 'Попробуйте число меньше.'

    if not message:
        message = f'Вы проиграли! Загаданное число было: {secret_number}'

    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
