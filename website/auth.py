from flask import Blueprint, render_template, request, flash

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
      flash('Account is created!', category='success')
      
  return render_template('singup.html')