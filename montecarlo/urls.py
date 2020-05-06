from django.urls import path
from .views import Montecarlo
app_name = 'montecarlo'

urlpatterns = [
    path('', Montecarlo.as_view(), name='montecarlo')
]
