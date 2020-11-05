from django.contrib import admin
from django.urls import path
from foodtaskerapp import views
from django.contrib.auth import views as auth_views





urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),


    path('restaurant/sign-in/', auth_views.LoginView.as_view(),
         {'template_name': 'restaurant/sign_in.html'},
         name ='restaurant-sign-in'),
    path('restaurant/sign-out', auth_views.LogoutView.as_view(),
         {'next_page': '/'},
         name = 'restaurant-sign-out'),
    path('restaurant/sign-up', views.restaurant_sign_up,
              name = 'restaurant-sign-up'),
    path('restaurant/', views.restaurant_home,
         name = 'restaurant-home')
]
