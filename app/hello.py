from flask import Flask, render_template
from datetime import datetime
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.moment import Moment

app = Flask(__name__)

moment = Moment(app)
bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
if __name__ == '__main__':
    manager.run()
    

