from flask import Flask, request, flash,url_for,make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap5
import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

todo = ['Comprar café','Enviar solicitud de compra ','Entregar producto']


@app.cli.command()
def test():
  tests = unittest.TestLoader().discover('test')
  unittest.TextTestRunner().run(tests)

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

@app.route('/hello', methods=['GET','POST'])
def hello():
  user_ip=session.get('user_ip')
  form=LoginForm(request.form)
  username = form.username.data

  context ={
    'user_ip': user_ip,
    'todos': todo,
    'login_form':form,
    'username':username
  }

  if request.method =='POST':
    username = form.username.data
    session['username']=username
    flash('Nombre se usuario registrado con exito')
    return redirect(url_for('hello'))

  return render_template('hello.html',**context)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
