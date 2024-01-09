from django.urls import path
from .views import RusumApiList, RusumApiDetail


urlpatterns = [
    path('', RusumApiList.as_view(), name='RusumApiList'),
    path('<int:id>/', RusumApiDetail.as_view(), name='RusumApiDetail'),
]