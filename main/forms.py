from django import forms
from .models import Customer, CustomerRow, Craftsman, CraftsmanRow, Worker, WorkerRow, FactoryRow

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
            'remaining': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الباقي', 'step': '0.01'}),
            'received': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'واصل', 'step': '0.01'}),
            'meters': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الأمتار', 'step': '0.01'}),
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
            'meters': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أمتار', 'step': '0.01'}),
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
            'remaining': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الباقي', 'step': '0.01'}),
            'received': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الواصل', 'step': '0.01'}),
            'classification': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'التصفية', 'step': '0.01'}),
        }


class FactoryRowForm(forms.ModelForm):
    class Meta:
        model = FactoryRow
        fields = ['received', 'expenses', 'goods', 'statement', 'note', 'date']
        widgets = {
            'received': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'واصل', 'step': '00.100'}),
            'expenses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'مصاريف', 'step': '00.100'}),
            'goods': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'بضاعة', 'step': '00.100'}),
            'statement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'بيان'}),
            'note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ملاحظة'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'التاريخ', 'type': 'date'}),
        }