from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todo = ['Comprar café','Enviar solicitud de compra ','Entregar producto']

class LoginForm(FlaskForm):
  username = StringField('Nombre de usuario', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html',error=error)


@app.route('/')
def index():
  user_ip = request.remote_addr
  response = make_response(redirect('/hello'))
  # response.set_cookie('user_ip',user_ip)
  session['user_ip']=user_ip
  return response

@app.route('/hello')
def hello():
  user_ip=session.get('user_ip')
  login_form = LoginForm()
  context ={
    'user_ip': user_ip,
    'todos': todo,
    'login_form':login_form
  }
  return render_template('hello.html',**context)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
