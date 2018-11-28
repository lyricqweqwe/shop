from django.conf.urls import url
from django.contrib import admin

from apps.home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

]
