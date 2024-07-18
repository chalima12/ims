from django.contrib import admin
from .admin_site import admin_site
from .models import Category, Stock, User, Item, Order, MaterialRequest, Notification
from .resources import StockResource
from import_export.admin import ImportExportModelAdmin

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

class StockAdmin(ImportExportModelAdmin):
    list_display = ('id','Stock_no', 'category', 'current_level')
    search_fields = ('category__name',)
    list_filter = ('category',)
    inlines = [ItemInline]
    resource_class = StockResource

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('user_name', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'password1', 'password2'),
        }),
    )
    list_display = ('user_name', 'first_name', 'last_name', 'is_staff')
    search_fields = ('user_name', 'first_name', 'last_name')
    ordering = ('user_name',)

class ItemAdmin(ImportExportModelAdmin):
    list_display = ('id', 'stock', 'name', 'description', 'price')
    search_fields = ('name', 'description')
    list_filter = ('stock__category',)

class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'stock', 'quantity', 'order_date', 'status')
    search_fields = ('status',)
    list_filter = ('order_date', 'status')
    actions = ['mark_as_shipped']

    def mark_as_shipped(self, request, queryset):
        queryset.update(status='shipped')
    mark_as_shipped.short_description = "Mark selected orders as shipped"

class MaterialRequestAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'item', 'request_date', 'status')
    search_fields = ('user__first_name', 'user__last_name', 'item__name', 'status')
    list_filter = ('request_date', 'status')

class NotificationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'message', 'notification_date')
    search_fields = ('user__first_name', 'user__last_name', 'message')
    list_filter = ('notification_date',)

# Register models with custom admin site
admin_site.register(Category, CategoryAdmin)
admin_site.register(Stock, StockAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Item, ItemAdmin)
admin_site.register(Order, OrderAdmin)
admin_site.register(MaterialRequest, MaterialRequestAdmin)
admin_site.register(Notification, NotificationAdmin)
