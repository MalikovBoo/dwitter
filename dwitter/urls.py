import django.contrib.auth.views as auth_views
from django.urls import path, include
from django.urls.base import reverse_lazy
from .views import dashboard, profile_list, profile, register

app_name = 'dwitter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(success_url='done'),
         name='password_change', ),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(success_url=reverse_lazy('dwitter:password_reset_done')),
         name="password_reset"),
    path('password_reset_done',
         auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('dwitter:password_reset_complete')),
         name="password_reset_confirm"),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
]

