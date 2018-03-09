from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index ():
    user = {'username': 'Cptn. Jack'}
    posts = [
    {

    'author': {'username': 'Barbosa'},
    'body': 'Ya best be believing in ghost stories Miss Elizabeth, you\'re in one'
    },
    {
    'author': {'username': 'Cptn_Hook1'},
    'body': 'I am the original, and the best captain'
    }


    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(
        form.username.data, form.remember_me.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
