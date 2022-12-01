from django.urls import path
from .views import (BlogHomePageView, PostDetailView)

urlpatterns=[
  path('', BlogHomePageView.as_view(), name = 'home'),
  path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]

app_name = 'base'