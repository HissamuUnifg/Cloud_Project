from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import RegisterForm

users = []

@app.route('/')
@app.route('/index')
def index():    
    return render_template('index.html', title='Home', users=users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('a new data has been appended')
        users.append(
            {
                'username': form.username.data,
                'email': form.email.data, 
                'senha': form.password.data
            },  
        )
        return redirect(url_for('index'))
    return render_template('register.html',  title='Register', form=form)
