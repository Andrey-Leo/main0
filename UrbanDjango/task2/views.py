from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("Все бастуют, а я учусь")

def index(request):
    return render(request, 'func_template.html')

class Index2(TemplateView):
    template_name = 'class_template.html'


