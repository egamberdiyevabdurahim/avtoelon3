from django.urls import path

from .views import YeyishiApiList, YeyishiApiDetail


urlpatterns = [
    path('', YeyishiApiList.as_view(), name='YeyishiApiList'),
    path('<int:id>/', YeyishiApiDetail.as_view(), name='YeyishiApiDetail'),
]