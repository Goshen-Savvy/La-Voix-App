from flask import render_template, url_for, flash, redirect
from MyBlogApp import app
from MyBlogApp.forms import RegistrationForm, LoginForm
from MyBlogApp.models import User, Post

posts = [
    {
        'author':'Anne Odeh',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'May 16 2020'
    },
    {
        'author':'Paulina Randy',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'May 17 2020'
    }
]
@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'anne@job.com' and form.password.data == 'jobb':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check your username and password!', 'danger')
    return render_template('login.html',title = 'Login', form=form)
