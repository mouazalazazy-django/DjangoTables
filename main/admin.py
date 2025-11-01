from django.contrib import admin
from .models import Customer, CustomerRow, Craftsman, CraftsmanRow, Worker, WorkerRow, FactoryRow

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
