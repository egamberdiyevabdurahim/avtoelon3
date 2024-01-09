from django.urls import path, include

from .views import ViloyatApiList, ViloyatApiDetail


urlpatterns = [
    path('', ViloyatApiList.as_view(), name='ViloyatApiList'),
    path('<int:id>', ViloyatApiDetail.as_view(), name='ViloyatApiDetail'),
    path('shahar/', include('avto.shahar_urls')),
]