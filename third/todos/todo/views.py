from django.shortcuts import render


def signupuser(request):  # регистрация пользователя
    return render(request, 'todo/signupuser.html')


def currenttodos(request):  #когда пользгователь зарегистрировался
    return render(request, 'todo/currenttodos.html')
