from . import db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  # data = request.form
  # print(data)
  return render_template('login.html', boolean=False)

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
  return '<p>Logout</p>'

@auth.route('/singup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form.get('email')
    userName = request.form.get('userName')
    password = request.form.get('password')
    confirmpassword = request.form.get('confirmpassword')

    if len(email) < 4:
      flash('Email is too short', category='error')
      
    elif len(userName) < 2:
      flash('First name must be greater than 1 character.', category='error')
    elif password != confirmpassword:
      flash('Passworld dont match', category='error')
    elif len(password) < 7:
      flash('Passwolrs is too short', category='error')
    else:
      new_user = User(email=email, userName=userName, password=generate_password_hash
      (password, method='sha256'))
      db.session.add(new_user)
      db.session.commit()
      flash('Account is created!', category='success')
      return redirect(url_for('views.home'))
      
  return render_template('singup.html')