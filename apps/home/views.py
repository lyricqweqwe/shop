from django.shortcuts import render
from django.views.decorators.cache import cache_page

from apps.home.models import *


# @cache_page(30)
def index(request):
    nav_list = Navigation.objects.all()
    pro_list = PropertyValue.objects.all()
    banner_list = Banner.objects.all()
    cate_list = Category.objects.all()
    for cate in cate_list:
        shops = cate.shop_set.all()
        for shop in shops:
            shop.img = shop.shopimage_set.values_list('shop_img_id', flat=True).first()
            cate.shops = shops
    return render(request, 'index.html', locals())
