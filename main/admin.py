from django.contrib import admin
from .models import Customer, CustomerRow, Craftsman, CraftsmanRow, Worker, WorkerRow, FactoryRow, LoginSession

class CustomerRowInline(admin.TabularInline):
    model = CustomerRow
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created_at']
    inlines = [CustomerRowInline]

class CraftsmanRowInline(admin.TabularInline):
    model = CraftsmanRow
    extra = 1

@admin.register(Craftsman)
class CraftsmanAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [CraftsmanRowInline]

class WorkerRowInline(admin.TabularInline):
    model = WorkerRow
    extra = 1

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [WorkerRowInline]

class FactoryRowInline(admin.TabularInline):
    model = FactoryRow
    extra = 1


@admin.register(LoginSession)
class LoginSessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'login_time', 'logout_time', 'ip_address']
    list_filter = ['user', 'login_time']
    search_fields = ['user__username', 'ip_address']
    readonly_fields = ['user', 'login_time', 'logout_time', 'ip_address', 'session_key']
    ordering = ['-login_time']
