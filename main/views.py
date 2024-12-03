from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        # header

        'title': 'Главная страница',
        'tel': ' 8(989)1234567',
        'work': 'Работаем без выходных 9 - 18',
        'logo': 'shiny',
        # intro

        'intro_content': 'В нашем магазине вы найдёте новогодние ёлочные игрушки из ваты и бумаги.',
        'intro_btn': 'каталог',
        # home_about

        'home_about_text': 'Мы специализируемся на создании уникальных и стильных ёлочных игрушек из экологически чистых материалов. Наша миссия — сделать праздник ярким и незабываемым для каждого . . .',
        'home_about_btn': 'Читать дальше',
        'home_about_title': 'О нас',
        # users_contacts

        'help': 'Не нашли что искали? Мы поможем!',
        'phone': 'Оставьте свой номер',
        'news': 'Будьте в курсе новостей и акций!',
        'email': 'Оставьте свою почту',
        # footer

        'img_info_1': 'Изображения на сайте от freepik',
        'img_info_2': 'Изображения товаров сгенерированы Алисой вместе с нейросетью YandexART',
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About page")
