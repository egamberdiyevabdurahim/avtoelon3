from django.urls import path

from .views import SignUp, Change


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('<int:id>', Change.as_view())
]