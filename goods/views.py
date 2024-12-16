from django.shortcuts import render

from goods.models import Categories, Products

def catalog(request):

    categories = Categories.objects.all()
    goods = Products.objects.all()

    context = {
        # header

        'title': 'Каталог',
        'tel': ' 8(989)1234567',
        'work': 'Работаем без выходных 9 - 18',
        'logo': 'shiny',
        # content

        'categories': categories,
        'goods': goods,
        # footer

        'img_info_1': 'Изображения на сайте от freepik',
        'img_info_2': 'Изображения товаров сгенерированы Алисой вместе с нейросетью YandexART',
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')