from django.conf.urls import url, include
from django.contrib import admin

from apps.home import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url('shop/',include('detail.urls')),
    url('111',include('search.urls'))
]
