from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name='الاسم')
    phone = models.CharField(max_length=20, verbose_name='رقم الهاتف')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'عميل'
        verbose_name_plural = 'العملاء'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class CustomerRow(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='rows', verbose_name='العميل')
    location = models.CharField(max_length=200, verbose_name='المكان')
    tex_meters = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='أمتار التكس')
    tex_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='سعر التكس')
    selek_meters = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='أمتار السيليكات')
    selek_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='سعر السيليكات')
    insulator_meters = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='أمتار العازل') 
    insulator_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='سعر العازل')
    repairs = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='مرمات')
    received = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='واصل')
    remaining = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='الباقي')
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='خصم')
    date = models.DateField(null=True, blank=True, verbose_name='التاريخ', default='لا يوجد')
    order = models.IntegerField(default=0, verbose_name='الترتيب')
    
    class Meta:
        verbose_name = 'صف العميل'
        verbose_name_plural = 'صفوف العملاء'
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"{self.customer.name} - {self.location}"

    def save(self, *args, **kwargs):
        self.remaining = self.tex_meters * self.tex_price + \
                         self.selek_meters * self.selek_price + \
                         self.insulator_meters * self.insulator_price + \
                         self.repairs - self.received - self.discount
        super().save(*args, **kwargs)

class Craftsman(models.Model):
    name = models.CharField(max_length=200, verbose_name='اسم الأسطى')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'أسطى'
        verbose_name_plural = 'الأسطوات'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class CraftsmanRow(models.Model):
    craftsman = models.ForeignKey(Craftsman, on_delete=models.CASCADE, related_name='rows', verbose_name='الأسطى')
    customer_name = models.CharField(max_length=200, verbose_name='اسم العميل')
    location = models.CharField(max_length=200, verbose_name='المكان')
    meters = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='أمتار')
    orders = models.CharField(max_length=200, verbose_name='طلبات')
    type = models.CharField(max_length=200, null=True, blank=True, verbose_name='النوع', default='لا يوجد')
    date = models.DateField(null=True, blank=True, verbose_name='التاريخ', default='لا يوجد')
    order = models.IntegerField(default=0, verbose_name='الترتيب')
    
    class Meta:
        verbose_name = 'صف الأسطى'
        verbose_name_plural = 'صفوف الأسطوات'
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"{self.craftsman.name} - {self.customer_name}"

class Worker(models.Model):
    name = models.CharField(max_length=200, verbose_name='اسم العامل')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'عامل'
        verbose_name_plural = 'العمال'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class WorkerRow(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='rows', verbose_name='العامل')
    classification = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='التصفية')
    received = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='الواصل')
    remaining = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='الباقي')
    date = models.DateField(null=True, blank=True, verbose_name='التاريخ', default='لا يوجد')
    order = models.IntegerField(default=0, verbose_name='الترتيب')
    
    class Meta:
        verbose_name = 'صف العامل'
        verbose_name_plural = 'صفوف العمال'
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"{self.worker.name} - {self.classification}"
        

class FactoryRow(models.Model):
    received = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='واصل')
    expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='مصاريف')
    goods = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='بضاعة')
    statement = models.CharField(max_length=200, default='لا يوجد', verbose_name='بيان')
    note = models.CharField(max_length=200, default='لا يوجد', verbose_name='ملاحظة')
    date = models.DateField(null=True, blank=True, verbose_name='التاريخ', default='لا يوجد')
    order = models.IntegerField(default=0, verbose_name='الترتيب')
    
    class Meta:
        verbose_name = 'صف المصنع'
        verbose_name_plural = 'صفوف المصنع'
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"المصنع - {self.date}"


class LoginSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_sessions', verbose_name='المستخدم')
    login_time = models.DateTimeField(auto_now_add=True, verbose_name='وقت تسجيل الدخول')
    logout_time = models.DateTimeField(null=True, blank=True, verbose_name='وقت تسجيل الخروج')
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name='عنوان IP')
    session_key = models.CharField(max_length=40, null=True, blank=True, verbose_name='مفتاح الجلسة')
    
    class Meta:
        verbose_name = 'جلسة تسجيل الدخول'
        verbose_name_plural = 'جلسات تسجيل الدخول'
        ordering = ['-login_time']
    
    def __str__(self):
        return f"{self.user.username} - {self.login_time}"
