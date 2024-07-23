from django.shortcuts import get_object_or_404, render
from django.views.generic import UpdateView, CreateView, DetailView, ListView, TemplateView
from .forms import*
from .models import*
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Stock, Order, User, Item
# views.py
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'  # Path to your custom login template
    

@staff_member_required
@login_required
def report_dashboard(request):
    # Fetch the data you want to display on the dashboard
    stock_count = Stock.objects.count()
    order_count = Order.objects.count()
    user_count = User.objects.count()
    item_count = Item.objects.count()
    
    # Example data for the dashboard
    data = {
        'stock_count': stock_count,
        'order_count': order_count,
        'user_count': user_count,
        'item_count': item_count,
    }
    
    return render(request, 'admin/report_dashboard.html', data)


class UserCreateView(LoginRequiredMixin,CreateView):
    model = User
    form_class=UserForm
    template_name = "warehouse/add-user.html"
    success_url = reverse_lazy('user')
    success_message = "User successfully created."
    


class UserListView(LoginRequiredMixin,ListView):
    model = User
    context_object_name='users'
    template_name = "warehouse/user.html"
class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserForm
    template_name = "warehouse/edit_user.html"
    success_url = reverse_lazy('user')


# views.py
from django.shortcuts import render, redirect
from .forms import OrderFormSet
@login_required
def create_orders(request):
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, queryset=Order.objects.none())
        if formset.is_valid():
            formset.save()
            return redirect('order_list')
        else:
            # Print errors to debug
            print("Formset errors:", formset.errors)
            for form in formset:
                print(form.errors)
    else:
        formset = OrderFormSet(queryset=Order.objects.none())

    return render(request, 'warehouse/add-order.html', {'formset': formset})



class OrderUpdateView(LoginRequiredMixin,UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "warehouse/edit-order.html"
    success_url = reverse_lazy('order_list')
    
class OrderListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'warehouse/order_list.html'
    context_object_name = 'orders'


class MaterialRequestCreateView(LoginRequiredMixin,CreateView):
    model = MaterialRequest
    form_class = MaterialRequestForm
    template_name = "warehouse/add-request.html"
    success_url = reverse_lazy('request_list')


class MaterialRequestUpdateView(LoginRequiredMixin,UpdateView):
    model = MaterialRequest
    form_class = MaterialRequestForm
    template_name = "warehouse/edit-request.html"
    success_url = reverse_lazy('request_list')
    
class MaterialRequestListView(LoginRequiredMixin,ListView):
    model = MaterialRequest
    template_name = 'warehouse/request_list.html'
    context_object_name = 'orders'
    
    
    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Notification


# views.py
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')

@csrf_exempt

def mark_notification_as_read(request):
    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        try:
            notification = Notification.objects.get(id=notification_id)
            notification.read = True
            notification.save()
            return JsonResponse({'status': 'success'})
        except Notification.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Notification not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

from django.http import JsonResponse
from .models import Notification
@login_required
def fetch_notifications(request):
    notifications = Notification.objects.filter(read=False,user=request.user)  # Adjust the queryset as needed
    notifications_data = []
    for notification in notifications:
        notifications_data.append({
            'id': notification.id,
            'message': notification.message,
            'notification_date': notification.notification_date.strftime('%Y-%m-%d'),
            'read': notification.read,
        })
    return JsonResponse({'notifications': notifications_data})








