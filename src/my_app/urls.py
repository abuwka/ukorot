from django.urls import path
from .views import test_view, redirect_view

app_name = 'app'

urlpatterns = [
    path("", test_view, name='test'),
    path("<str:new_link>/", redirect_view, name='redir')
]

