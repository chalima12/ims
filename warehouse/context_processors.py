# context_processors.py
from .models import Notification

def notifications_processor(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user,read=False).order_by('-id')
        notification = Notification.objects.filter(user=request.user,read=False).count()
        
    else:
        notifications = []
        notification =0
      
    return {'notifications': notifications}