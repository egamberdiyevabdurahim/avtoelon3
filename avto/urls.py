from django.urls import path, include

from .views import AvtoApiList, AvtoApiDetail


urlpatterns = [
    path('', AvtoApiList.as_view(), name='AvtoApiList'),
    path('<int:id>/', AvtoApiDetail.as_view(), name='AvtoApiDetail'),
    path('photo/', include('avto.photo_urls')),
    path('davlat/', include('avto.davlat_urls')),
    path('model/', include('avto.model_urls')),
    path('karobka/', include('avto.karobka_urls')),
    path('rang/', include('avto.rang_urls')),
    path('yeyishi/', include('avto.yeyishi_urls')),
]