from django.urls import path
from rest_framework.authtoken import views

from .views import SignUp, Change, Login, LikeAvto


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('<int:id>', Change.as_view()),
    path('login/', Login.as_view(), name='login'),
    path('likeavto/<int:id>', LikeAvto.as_view(), name='like'),
    # path('login/', views)
]