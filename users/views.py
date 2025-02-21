from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Direccion
from django.http import JsonResponse
import json
from django import forms

def usersIndex(request):
    users = User.objects.all()
    return render(request, "users/index.html", {"users": users})

def createUserView(request):
    return render(request, "users/create.html")

def createUserByFetch(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return JsonResponse({"NOMBRE_RECIBIDO": body.get("name")})

def createUser(request):
    data = {}
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            age = request.POST.get("age")
            rfc = request.POST.get("rfc")
            photo = request.FILES.get("photo")
            user = User(name=name, email=email, age=age, rfc=rfc, photo=photo)
            user.save()
            data["user"] = user
            data["message"] = "User created successfully"
            data["status"] = "success"
    except Exception as e:
        data["message"] = str(e)
        data["status"] = "error"

def userDetail(request, id):
    user = get_object_or_404(User, id=id)
    direcciones = Direccion.objects.filter(usuario=user)

    if request.method == 'POST':
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.age = request.POST['age']
        user.rfc = request.POST['rfc']
        user.photo = request.POST['photo']
        user.save()
        return redirect('users_index')
    
    return render(request, "users/detail.html", {"user": user, 'direcciones': direcciones})

def crear_direccion(request, user_id):  # Movida fuera de userDetail
    user = get_object_or_404(User, pk=user_id)

    class DireccionForm(forms.Form):
        calle = forms.CharField(max_length=100)
        numero = forms.CharField(max_length=20)
        colonia = forms.CharField(max_length=100)

    if request.method == 'POST':
        form = DireccionForm(request.POST)
        if form.is_valid():
            direccion = Direccion(
                usuario=user,
                calle=form.cleaned_data['calle'],
                numero=form.cleaned_data['numero'],
                colonia=form.cleaned_data['colonia']
            )
            direccion.save()
            return redirect('userDetail', user_id=user_id)
    else:
        form = DireccionForm()

    return render(request, 'users/crear_direccion.html', {'form': form, 'user': user})