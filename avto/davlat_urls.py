from django.urls import path, include

from .views import DavlatApiList, DavlatApiDetail


urlpatterns = [
    path('', DavlatApiList.as_view(), name='DavlatApiList'),
    path('<int:id>', DavlatApiDetail.as_view(), name='DavlatApiDetail'),
    path('viloyat/', include('avto.viloyat_urls')),
]