from django.shortcuts import render

def platform(request):
    return render(request, 'platform.html')

def games(request):
    name_game = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'name_game': name_game,
    }
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')
