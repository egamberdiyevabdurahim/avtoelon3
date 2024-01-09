from django.urls import path

from .views import KarobkaApiList, KarobkaApiDetail


urlpatterns = [
    path('', KarobkaApiList.as_view(), name='KarobkaApiList'),
    path('<int:id>/', KarobkaApiDetail.as_view(), name='KarobkaApiDetail'),
]