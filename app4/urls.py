from django.contrib import admin
from django.urls import path
from . import views
from app4.views import LoginListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard',views.dashboard, name='dashboard'),
     path('api/logins/', LoginListView.as_view(), name='login-list'),
]