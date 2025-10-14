# Management System - نظام الإدارة

## Overview

نظام إدارة متكامل مبني على Django 5.2.7 لإدارة ثلاثة أنواع من الكيانات:
- **العملاء (Customers)**: مع تتبع المواقع والأمتار والمبالغ المستلمة والمتبقية
- **الأسطوات (Craftsmen)**: مع تعيينات العملاء والمواقع والأمتار والطلبات
- **العمال (Workers)**: مع التصنيف والمبالغ المستلمة والمتبقية

## Features المميزات

### العملاء (Customers)
- عرض جداول منفصلة لكل عميل
- الاسم ورقم الهاتف يظهران فوق الجدول
- أعمدة: المكان، الأمتار، واصل، الباقي
- حساب تلقائي للمجموع الكلي (واصل + باقي)
- **ميزة الطباعة**: إمكانية طباعة جدول العميل كـ PDF بنفس التنسيق
- إضافة، تعديل، وحذف الصفوف

### الأسطوات (Craftsmen)
- عرض جداول منفصلة لكل أسطى
- اسم الأسطى يظهر فوق الجدول
- أعمدة: اسم العميل، المكان، أمتار، طلبات
- إضافة، تعديل، وحذف الصفوف

### العمال (Workers)
- عرض جداول منفصلة لكل عامل
- اسم العامل يظهر فوق الجدول
- أعمدة: التصفية، الواصل، الباقي
- إضافة، تعديل، وحذف الصفوف

## User Preferences

- لغة التواصل: العربية
- أسلوب التواصل: بسيط وواضح

## Technical Architecture

### Backend
- **Framework**: Django 5.2.7
- **Database**: SQLite (قابل للتحويل إلى PostgreSQL أو MySQL)
- **Pattern**: MTV (Model-Template-View)

### Models
```python
Customer → CustomerRow (one-to-many)
- Customer: name, phone
- CustomerRow: location, meters, received, remaining, order

Craftsman → CraftsmanRow (one-to-many)
- Craftsman: name
- CraftsmanRow: customer_name, location, meters, orders, order

Worker → WorkerRow (one-to-many)
- Worker: name
- WorkerRow: classification, received, remaining, order
```

### Frontend
- **Templates**: Django Templates with RTL support
- **Styling**: Custom CSS مع دعم كامل للعربية و RTL
- **Design**: Card-based UI with responsive tables
- **Navigation**: Top navbar with links to all sections

### Security
- CSRF protection enabled for all forms
- POST-only delete operations (protected by @require_POST)
- Form validation using Django forms

### PDF Generation
- **Library**: ReportLab
- **Arabic Support**: arabic-reshaper + python-bidi
- **Format**: A4, table-based layout
- **Available for**: Customer tables only

### URL Structure
```
/                          → Home page
/customers/                → Customer list
/customers/{id}/           → Customer detail with table
/customers/{id}/print/     → Print customer table as PDF
/customer-row/{id}/edit/   → Edit customer row
/customer-row/{id}/delete/ → Delete customer row (POST)

/craftsmen/                → Craftsman list
/craftsmen/{id}/           → Craftsman detail with table
/craftsman-row/{id}/edit/  → Edit craftsman row
/craftsman-row/{id}/delete/→ Delete craftsman row (POST)

/workers/                  → Worker list
/workers/{id}/             → Worker detail with table
/worker-row/{id}/edit/     → Edit worker row
/worker-row/{id}/delete/   → Delete worker row (POST)
```

## Dependencies

### Core
- django==5.2.7
- pillow==11.3.0

### PDF Generation
- reportlab==4.4.4
- arabic-reshaper==3.0.0
- python-bidi==0.6.6

## Recent Changes (October 14, 2025)

1. ✅ إنشاء نظام Django كامل من الصفر
2. ✅ إنشاء نماذج البيانات للعملاء والأسطوات والعمال
3. ✅ إنشاء واجهة عربية كاملة مع دعم RTL
4. ✅ إضافة وظيفة الطباعة للعملاء
5. ✅ إصلاح ثغرة CSRF في عمليات الحذف (تحويل من GET إلى POST)
6. ✅ إصلاح وظيفة الطباعة لدعم إرجاع PDF صحيح
7. ✅ تطبيق CRUD كامل (إضافة، عرض، تعديل، حذف) لجميع الكيانات

## How to Run

```bash
python manage.py runserver 0.0.0.0:5000
```

Server will be available at: http://0.0.0.0:5000/

## Future Enhancements

- إضافة نظام بحث وتصفية
- إضافة الطباعة للأسطوات والعمال
- إضافة تصدير إلى Excel
- إضافة لوحة تحكم بإحصائيات
- إضافة نظام مستخدمين ومصادقة
- إضافة نسخ احتياطي واستعادة البيانات
