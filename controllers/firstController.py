# -*- coding: utf-8 -*-
# intente algo como
def index(): 
    return dict(message="hello from firstController.py")

def saludo():
    variable = request.args # obtiene las variables en forma de array, que vengan por la url
    response.view='saludo.html' # selecciona una vista
    mensaje = "hola mundo, desde saludo"
    return dict(mensaje=mensaje, variable=variable)

def hello2():
    response.flash=T("Hello World in a flash!")
    return dict(message=T("Hello World"))

# muestra estatus
def status():
    return dict(toobar=response.toolbar())

# para redireccionar
def redirectme():
    redirect(URL('hello2'))

def raiseexception():
    1 / 0
    response.view = 'saludo.html'
    return dict(mensaje='oops')

def servejs():
    import gluon.contenttype
    response.headers['Content-Type']=gluon.contenttype.contenttype('.js')
    return 'alert("This is a Javascript document, it is not supposed to run!");'

def makejson():
    return response.json(['foo', {'bar': ('baz', None, 1.0, 2)}])


def makertf():
    import gluon.contrib.pyrtf as q
    doc=q.Document()
    section=q.Section()
    doc.Sections.append(section)
    section.append('Section Title')
    section.append('web2py is great. '*100)
    response.headers['Content-Type']='text/rtf'
    return q.dumps(doc)
