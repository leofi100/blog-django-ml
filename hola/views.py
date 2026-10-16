from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Articulo
from .forms import ArticuloForm
from .models import Mensaje
import joblib

modelo = joblib.load("modelo_clientes.pkl")

def hola_mundo(request):
    articulos = Articulo.objects.all()
    contexto = {'articulos': articulos}
    return render(request, 'hola/hola_mundo.html', contexto)

@login_required  # ← Solo usuarios registrados pueden acceder
def nuevo_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user  # ← Asignar el autor
            articulo.save()
            return redirect('hola_mundo')
    else:
        form = ArticuloForm()
    
    contexto = {'form': form}
    return render(request, 'hola/nuevo.html', contexto)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ← Iniciar sesión automáticamente
            return redirect('hola_mundo')
    else:
        form = UserCreationForm()
    
    contexto = {'form': form}
    return render(request, 'hola/registro.html', contexto)

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('hola_mundo')
    else:
        form = AuthenticationForm()
    
    contexto = {'form': form}
    return render(request, 'hola/login.html', contexto)

def cerrar_sesion(request):
    logout(request)
    return redirect('hola_mundo')


def detalle_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    contexto = {'articulo': articulo}
    return render(request, 'hola/detalle.html', contexto)


@login_required
def editar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    
    # Verificar que solo el autor pueda editar
    if articulo.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este artículo")
    
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('detalle_articulo', id=articulo.id)
    else:
        form = ArticuloForm(instance=articulo)
    
    contexto = {'form': form, 'articulo': articulo}
    return render(request, 'hola/editar.html', contexto)

@login_required
def eliminar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    
    # Verificar que solo el autor pueda eliminar
    if articulo.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este artículo")
    
    if request.method == 'POST':
        articulo.delete()
        return redirect('hola_mundo')
    
    contexto = {'articulo': articulo}
    return render(request, 'hola/eliminar.html', contexto)

def contacto(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        Mensaje.objects.create(nombre=nombre, email=email)   # ← guarda en la BD
        return redirect("contacto")
    return render(request, "contacto.html")

@login_required
def ver_mensajes(request):
#    mensajes = Mensaje.objects.all() 
    mensajes = Mensaje.objects.all().order_by("-fecha_mensaje")                  
    return render(request, "mensajes.html", {"mensajes": mensajes})


def predecir_cliente(request):
    resultado = None
    if request.method == "POST":
        edad = int(request.POST["edad"])
        minutos = int(request.POST["minutos"])
        prediccion = modelo.predict([[edad, minutos]])
        resultado = "SÍ comprará" if prediccion[0] == 1 else "NO comprará"
    return render(request, "predecir.html", {"resultado": resultado})
