from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


User = get_user_model()


@login_required
def area_reservada(request):
    return render(request, 'usuarios/area.html', {'usuario': request.user})

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email', '')
        telefono = request.POST.get('telefono', '')

        # Crear usuario
        User.objects.create_user(username=username, password=password, email=email, telefono=telefono)
        return redirect('login')  # después de crear, va al login

    return render(request, 'usuarios/registro.html')