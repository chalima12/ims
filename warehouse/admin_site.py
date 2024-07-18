from django.contrib.admin import AdminSite
from django.urls import path
from .views import report_dashboard
from django.utils.translation import gettext_lazy as _

class MyAdminSite(AdminSite):
    site_header = _("IMS Administration")
    site_title = _("IMS Admin")
    index_title = _("Welcome to IMS Admin Panel")

    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('report-dashboard/', self.admin_view(report_dashboard), name='report-dashboard'),
        ]
        return custom_urls + urls

admin_site = MyAdminSite(name='myadmin')
