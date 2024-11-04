from django.shortcuts import render
from .models import Materia

# Create your views here.
def inicio_vista(request):
    LasMaterias=Materia.objects.all()
    return render(request,"GestionarMateria.html")