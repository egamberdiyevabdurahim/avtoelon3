from django.urls import path

from .views import PhotoApiList, PhotoApiDetail


urlpatterns = [
    path('', PhotoApiList.as_view(), name='PhotoApiList'),
    path('<int:id>/', PhotoApiDetail.as_view(), name='PhotoApiDetail'),
]