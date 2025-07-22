
from django.shortcuts import render, redirect
from .models import Perro

from .forms import PerroForm

# Create your views here.
def home(request):
    filtro = request.GET.get('estado')
    perros = Perro.objects.all()
    if filtro:
        perros = perros.filter(estado=filtro)
    return render(request, 'perros/home.html', {'perros': perros})



def publicar_perro(request):
    if request.method == 'POST':
        form = PerroForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_perro = form.save()
            print(f"Perro guardado: {nuevo_perro}")
            return redirect('home')
    else:
        form = PerroForm()
    return render(request, 'perros/formulario.html', {'form': form})
