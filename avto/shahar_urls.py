from django.urls import path

from .views import ShaharApiList, ShaharApiDetail


urlpatterns = [
    path('', ShaharApiList.as_view(), name='ShaharApiList'),
    path('<int:id>/', ShaharApiDetail.as_view(), name='ShaharApiDetail'),
]