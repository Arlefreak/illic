from django.conf.urls import url, include
from django.contrib import admin
from cms import views
from blog import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^blog/', include(urls)),
]
