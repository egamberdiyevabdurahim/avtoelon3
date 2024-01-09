from django.urls import path, include

from .views import ModelApiList, ModelApiDetail


urlpatterns = [
    path('', ModelApiList.as_view(), name='ModelApiList'),
    path('<int:id>/', ModelApiDetail.as_view(), name='ModelApiDetail'),
    path('rusum/', include('avto.rusum_urls')),
]