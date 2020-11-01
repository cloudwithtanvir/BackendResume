from django.urls import path
from . import views

from .views import homePageView

# from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('api/drop/', login_required(views.DropListCreate.as_view()) ),
    path('api/drop/', views.DropListCreate.as_view()) ,
    path('api/refer/', views.refer),
    # path('api/year/',views.exp_year),
    path('', homePageView, name='home'),
]