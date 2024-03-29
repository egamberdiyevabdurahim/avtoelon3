from django.urls import path, include

from .views import AvtoApiList, AvtoApiDetail, AllApiList


urlpatterns = [
    path('all/', AllApiList.as_view(), name='all'),
    path('', AvtoApiList.as_view(), name='AvtoApiList'),
    path('<int:id>/', AvtoApiDetail.as_view(), name='AvtoApiDetail'),
    path('photo/', include('avto.photo_urls')),
    # path('davlat/', include('avto.davlat_urls')),
    path('model/', include('avto.model_urls')),
]