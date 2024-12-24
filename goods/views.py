from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from goods.models import Categories, Products

def catalog(request, category_slug, page=1):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products, category__slug=category_slug)

    paginator = Paginator(goods, 4)
    current_page = paginator.page(page)

    categories = Categories.objects.all()

    context = {
        # header

        'title': 'Каталог',
        'tel': ' 8(989)1234567',
        'work': 'Работаем без выходных 9 - 18',
        'logo': 'shiny',
        # content

        'categories': categories,
        'goods': current_page,
        'slug_url': category_slug,
        # footer

        'img_info_1': 'Изображения на сайте от freepik',
        'img_info_2': 'Изображения товаров сгенерированы Алисой вместе с нейросетью YandexART',
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):

    product: Products = Products.objects.get(slug=product_slug)

    context = {
        # header

        # 'title': 'Каталог',
        'tel': ' 8(989)1234567',
        'work': 'Работаем без выходных 9 - 18',
        'logo': 'shiny',
        # content
        'product': product,
        # footer

        'img_info_1': 'Изображения на сайте от freepik',
        'img_info_2': 'Изображения товаров сгенерированы Алисой вместе с нейросетью YandexART',
    }
    return render(request, 'goods/product.html', context)