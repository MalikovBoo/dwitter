import django.contrib.auth.views
from django.urls import path, include
from .views import dashboard, profile_list, profile

app_name = 'dwitter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_change/', django.contrib.auth.views.PasswordChangeView.as_view(success_url='done'), name='password_change', ),
    path('password_change/done/', django.contrib.auth.views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
]

