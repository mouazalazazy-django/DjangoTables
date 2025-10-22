from django import forms
from .models import Customer, CustomerRow, Craftsman, CraftsmanRow, Worker, WorkerRow

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العميل'}),
        }

class CustomerRowForm(forms.ModelForm):
    class Meta:
        model = CustomerRow
        fields = ['location', 'meters', 'type', 'received', 'remaining', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'التاريخ', 'type': 'date'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'النوع'}),
            'remaining': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الباقي', 'step': '100.00'}),
            'received': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'واصل', 'step': '100.00'}),
            'meters': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الأمتار', 'step': '100.00'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المكان'}),
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
        fields = ['customer_name', 'location', 'meters', 'type', 'orders', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'التاريخ', 'type': 'date'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'النوع'}),
            'orders': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'طلبات'}),
            'meters': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أمتار', 'step': '100.00'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المكان'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العميل'}),
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
        fields = ['classification', 'received', 'remaining', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'التاريخ', 'type': 'date'}),
            'remaining': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الباقي', 'step': '100.00'}),
            'received': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الواصل', 'step': '100.00'}),
            'classification': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'التصفية', 'step': '100.00'}),
        }
