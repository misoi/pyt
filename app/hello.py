from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI' ] =\'sqlite:///' + os.path.join(basedir, 'data.sqlite') #database url
app.config['SQLALCHEMY_COMMIT_ON_TEARDWON']=True #enable automatic commits of database changes at the end of each request.

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name') #gets the last name of the user
        if old_name is not None and old_name != form.name.data: #gives the conditions of name
            flash('looks like you have changed your name')# response given if the name is not found
        session['name'] = form.name.data # helps apps remember things by storing user sessions at the client-side cookies
        form.name.data=''
        return render_template(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))



if __name__ == '__main__':
    manager.run()


