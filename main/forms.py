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
        fields = ['location', 'tex_meters', 'tex_price', 'selek_meters', 'selek_price', 'insulator_meters', 'insulator_price', 'repairs', 'received', 'date']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المكان'}),
            'tex_meters': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أمتار التكس', 'step': '0.01'}),
            'tex_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سعر التكس', 'step': '0.01'}),
            'selek_meters': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أمتار السيليكات', 'step': '0.01'}),
            'selek_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سعر السيليكات', 'step': '0.01'}),
            'insulator_meters': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أمتار العازل', 'step': '0.01'}),
            'insulator_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سعر العازل', 'step': '0.01'}),
            'repairs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'مرمات', 'step': '0.01'}),
            'received': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'واصل', 'step': '0.01'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'التاريخ', 'type': 'date'}),
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