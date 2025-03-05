from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game, News


def platform(request):
    return render(request, 'platform.html')


def games(request):
    name_game = Game.objects.all()
    context = {
            'name_game': name_game,
    }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')


def sign_up_by_django(request):
    info = {}  # пустой словарь для передачи в context функции render
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif Buyer.objects.filter(name=name).exists():  # проверяем, существует ли пользователь в базе данных
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            Buyer.objects.create(name=name, balance=0, age=age)  # создаем нового пользователя в базе данных
            return HttpResponse(f'Приветствуем {name}')
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}  # пустой словарь для передачи в context функции render
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif Buyer.objects.filter(name=name).exists():  # проверяем, существует ли пользователь в базе данных
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            Buyer.objects.create(name=name, balance=0, age=age)  # создаем нового пользователя в базе данных
            return HttpResponse(f'Приветствуем {name}')
    return render(request, 'registration_page.html', info)


def news(request):
    new = News.objects.all().order_by('-date')
    paginator = Paginator(new, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})

