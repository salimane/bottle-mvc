# -*- coding: utf-8 -*-
from project import app
from bottle import static_file, template, request

@app.route('/', method = 'GET')
def index():
  return template('printer/index', message = '')

@app.route('/:file#(favicon.ico|humans.txt)#')
def favicon(file):
  return static_file(file, root = 'project/static/misc')

@app.route('/:path#(images|css|js|fonts)\/.+#')
def server_static(path):
  return static_file(path, root = 'project/static')

@app.route('/print', method = ['GET','POST'])
def printer():
  if request.method == 'POST':
    from project.models.Printer import Printer
    printer = Printer()
    message = printer.show_string(request.forms.get('text'))
    return template('printer/index', message = message)
  return template('printer/print', message = '')


