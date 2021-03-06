from app import app
from flask import render_template, flash, url_for, redirect
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Open Shelf', user='Anish')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested by the {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form = form)






