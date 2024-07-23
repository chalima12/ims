from.views import *
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('', landing_page, name='landing_page'),
  
  path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/add-order/', create_orders, name='add-order'),
    path('orders/edit-order/<int:pk>/', OrderUpdateView.as_view(), name='edit_order'),
    
     path('requests/', MaterialRequestListView.as_view(), name='request_list'),
    path('requests/add-request/', MaterialRequestCreateView.as_view(), name='add-request'),
    path('requests/edit-resquest/<int:pk>/', MaterialRequestUpdateView.as_view(), name='edit_request'),
     path('mark_notification_as_read/', mark_notification_as_read, name='mark_notification_as_read'),
     path('fetch-notifications/', fetch_notifications, name='fetch_notifications'),
    
   path('user/add-user/', UserCreateView.as_view(),name='add-user'),
   path('user/', UserListView.as_view(),name='user'),
    path('user/user/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
   path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
]