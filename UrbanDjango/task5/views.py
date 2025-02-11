from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister





def sign_up_by_django(request):
    users = ['User1', 'User2', 'User3']
    info = {}  # пустой словарь для передачи в context функции render
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            users.append(username)
            return HttpResponse(f'Приветствуем {username}')
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    users = ['User1', 'User2', 'User3']
    info = {}  # пустой словарь для передачи в context функции render
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            users.append(username)
            return HttpResponse(f'Приветствуем {username}')
    return render(request, 'registration_page.html', info)
