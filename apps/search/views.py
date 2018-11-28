from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from apps.home.models import *


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入搜索词'
        return render(request, 'search.html', {'error_msg': error_msg})
    shops = Shop.objects.filter(Q(name__icontains=q)|Q(sub_title__icontains=q))
    for shop in shops:
        shop.img =shop.shopimage_set.values_list('shop_img_id',flat=True).first()
    if not shops:
        error_msg = '商品不存在,请重新使用关键字搜索'
        return render(request, 'search.html', {'error_msg': error_msg})
    return render(request,'search.html',{'shops':shops})

