from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, DetailView, ListView, TemplateView
from .forms import*
from .models import*

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


class UserCreateView(CreateView):
    model = User
    form_class=UserForm
    template_name = "warehouse/add-user.html"
    success_url = reverse_lazy('user')
    success_message = "User successfully created."
    


class UserListView(ListView):
    model = User
    context_object_name='users'
    template_name = "warehouse/user.html"
class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "warehouse/edit_user.html"
    success_url = reverse_lazy('user')



from .forms import OrderForm

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "warehouse/add-order.html"
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "warehouse/edit-order.html"
    success_url = reverse_lazy('order_list')
    
class OrderListView(ListView):
    model = Order
    template_name = 'warehouse/order_list.html'
    context_object_name = 'orders'