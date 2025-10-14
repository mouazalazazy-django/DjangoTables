from django import forms
from .models import Customer, CustomerRow, Craftsman, CraftsmanRow, Worker, WorkerRow

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العميل'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),
        }

class CustomerRowForm(forms.ModelForm):
    class Meta:
        model = CustomerRow
        fields = ['location', 'meters', 'received', 'remaining']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المكان'}),
            'meters': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الأمتار', 'step': '0.01'}),
            'received': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'واصل', 'step': '0.01'}),
            'remaining': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الباقي', 'step': '0.01'}),
        }

class CraftsmanForm(forms.ModelForm):
    class Meta:
        model = Craftsman
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم الأسطى'}),
        }

class CraftsmanRowForm(forms.ModelForm):
    class Meta:
        model = CraftsmanRow
        fields = ['customer_name', 'location', 'meters', 'orders']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العميل'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المكان'}),
            'meters': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أمتار', 'step': '0.01'}),
            'orders': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'طلبات'}),
        }

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العامل'}),
        }

class WorkerRowForm(forms.ModelForm):
    class Meta:
        model = WorkerRow
        fields = ['classification', 'received', 'remaining']
        widgets = {
            'classification': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'التصفية', 'step': '0.01'}),
            'received': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الواصل', 'step': '0.01'}),
            'remaining': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الباقي', 'step': '0.01'}),
        }
