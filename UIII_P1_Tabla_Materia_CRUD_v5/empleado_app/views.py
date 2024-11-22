from django.shortcuts import render
from .models import Empleados
# Create your views here.

def inicio_vista(request):
    losempleados=Empleados.objects.all()
    return render(request,"gestionarEmpleados.html",{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["txtempleado"]
    nombre=request.POST["txtnombre"]
    email=request.POST["txtemail"]
    curp=request.POST["txtcurp"]
    acta_de_nacimiento=request.POST["txtnacimiento"]
    numero_celular=request.POST["txtnum"]
    rfc=request.POST["txtrfc"]
    id_sucursales=request.POST["txtsucursales"]
    direccion=request.POST["txtdireccion"]

    guardarempleados=Empleados.objects.create(
        id_empleado=id_empleado,nombre=nombre,email=email,curp=curp,acta_de_nacimiento=acta_de_nacimiento,numero_celular=numero_celular,rfc=rfc,id_sucursales=id_sucursales,direccion=direccion
    ) # GUARDA EL REGISTRO

    return redirect("/")

def seleccionarEmpleado(request,id_empleado):
    empledo=Empleados.objects.get(id_empleado=id_empleado)
    return render(request,"editarempleado.html",{"misempleados":empledo})

def editarEmpleado(request):
    id_empleado=request.POST["txtempleado"]
    nombre=request.POST["txtnombre"]
    email=request.POST["txtemail"]
    curp=request.POST["txtcurp"]
    acta_de_nacimiento=request.POST["txtnacimiento"]
    numero_celular=request.POST["txtnum"]
    rfc=request.POST["txtrfc"]
    id_sucursales=request.POST["txtsucursales"]
    direccion=request.POST["txtdireccion"]
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    empleado.nombre=nombre
    empleado.email=email
    empleado.curp=curp
    empleado.acta_de_nacimiento=acta_de_nacimiento
    empleado.numero_celular=numero_celular
    empleado.rfc=rfc
    empleado.id_sucursales=id_sucursales
    empleado.direccion=direccion
    empleado.save() # GUARDA EL REGISTRO
    return redirect("/")

def borrarEmpleado (request,id_empleado):
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    empleado.delete() # ELIMINA EL REGISTRO
    return redirect("/")