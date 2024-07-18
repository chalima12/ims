from.views import *
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('user/add-user/', UserCreateView.as_view(),name='add-user'),
   path('user/', UserListView.as_view(),name='user'),
    path('user/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
   path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
]