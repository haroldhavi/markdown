from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido =apellido

def saludo(request): #"primera vista"
    
    p1= Persona(" profesor harold", "virguez")
#    nombre= "Harold"

 #   apellido="Virguez"
    ahora= datetime.datetime.now()

    doc_externo =open("/home/harold/Escritorio/26defebrero/proyecto/proyecto/plantillas/miplantilla.html")

    plt =Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora})

    documento=plt.render(ctx)
    
    return HttpResponse(documento)

def adios(request):
    return HttpResponse ("adios")

def hora (request):
    fecha_actual= datetime.datetime.now()

    documento = """<html> 
    <boddy> 
    <p>fecha y hora actuales %s
    <p/> 
    <boddy/> 
    <html/>""" %fecha_actual

    return HttpResponse(documento)

def calcula_edad(request, edad, agno):

#    edadactual = 24
    periodo=agno-2021
    edad_futura =edad+periodo
    documento = "<html><boddy><h2>En el año %s tendras %s años" %(agno, edad_futura)
    return HttpResponse(documento)


