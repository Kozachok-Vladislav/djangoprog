from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from of_str_selstroiproekt.models import Of_str_selstroiproekt


def index(request):
    posts = Of_str_selstroiproekt.objects.all()
    context = {
        'posts' : posts ,
        'menu' : menu ,
        'title' : 'Главная страница',

    }

    return render (request, 'of_str_selstroiproekt/index.html' ,context=context)


def about(request):
    return render(request, 'of_str_selstroiproekt/about.html' , { 'title' : 'О сайте'})


def contact(request):
    return HttpResponse("Обратная связь")


def vakansii(request):
    return HttpResponse("Вакансии")


def news(request, news):
    return HttpResponse(f"Отображение новости с id{news}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

menu = [{'title' :"Наша деятельность" , 'url_name' : 'about'} ,
        {'title' : "Контакты" ,'url_name' : contact} ,
        {'title' : "Вакансии" , 'url_name' : vakansii} ,
]
