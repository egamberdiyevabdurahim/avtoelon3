from django.urls import path

from .views import RangApiList, RangApiDetail


urlpatterns = [
    path('', RangApiList.as_view(), name='RangApiList'),
    path('<int:id>/', RangApiDetail.as_view(), name='RangApiDetail'),
]