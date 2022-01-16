from ast import If
import email
from re import U
from . import db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email =request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        flash('Logged in successfully!', category='success')
        login_user(user, remember=True)
        return redirect(url_for('views.home'))
      else:
        flash('Invalid password, try again!', category='error')
    else:
      flash('Emai does not exist!', category='error')

  return render_template('login.html', user=current_user)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))

@auth.route('/singup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form.get('email')
    userName = request.form.get('userName')
    password = request.form.get('password')
    confirmpassword = request.form.get('confirmpassword')

    user = User.query.filter_by(email=email).first()
    if user:
      flash('Email allready exist', category='error')

    elif len(email) < 4:
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
      login_user(user, remember=True)
      flash('Account is created!', category='success')
      return redirect(url_for('views.home'))
      
  return render_template('singup.html', user=current_user)