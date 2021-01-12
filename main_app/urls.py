from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('developers/', views.developers_index, name='index'),
    path('developers/<int:developer_id>/', views.developers_detail, name='detail'),
    path('developers/create/', views.DeveloperCreate.as_view(), name='developers_create'),
    path('accounts/', include('django.contrib.auth.urls')),
]
