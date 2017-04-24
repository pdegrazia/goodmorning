from flask import Flask, render_template
from flask_ask import Ask, statement, question
import random
import logging

app = Flask(__name__)
ask = Ask(app, '/')

logging.basicConfig()

SENTENCES = ['You are the most beautiful!', 'Good morning my love!',
             'Have a wonderful day!', 'I Love You to the moon and back!']


@ask.launch
def welcome():
    sentence = SENTENCES[random.randint(0,len(SENTENCES)-1)]
    return statement(sentence)


if __name__ == '__main__':
    app.run(debug=True)