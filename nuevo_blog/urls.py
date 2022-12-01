from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve
from .views import(HomePageView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('base/',include('aplicaciones.base.urls',  namespace='base')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve , {
            'document_root':settings.MEDIA_ROOT,
        }),
    ]