from django.contrib import admin

from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'courier', 'status', 'total_price', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username', 'courier__username')
    inlines = [OrderItemInline]

    def save_model(self, request, obj, form, change):
        obj.save()
        obj.calculate_total_price()
