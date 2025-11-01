from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Customer, CustomerRow, Craftsman, CraftsmanRow, Worker, WorkerRow, FactoryRow
from .forms import CustomerForm, CustomerRowForm, CraftsmanForm, CraftsmanRowForm, WorkerForm, WorkerRowForm, FactoryRowForm
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from arabic_reshaper import reshape
from bidi.algorithm import get_display
import io


def home(request):
    return render(request, 'main/home.html')


def customer_list(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة العميل بنجاح')
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'main/customer_list.html', {'customers': customers, 'form': form})


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    rows = customer.rows.all()

    total_received = sum(row.received for row in rows)
    total_remaining = sum(row.remaining for row in rows)

    if request.method == 'POST':
        form = CustomerRowForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.customer = customer
            row.order = customer.rows.count()
            row.save()
            messages.success(request, 'تم إضافة الصف بنجاح')
            return redirect('customer_detail', pk=pk)
    else:
        form = CustomerRowForm()

    context = {
        'customer': customer,
        'rows': rows,
        'form': form,
        'total_received': total_received,
        'total_remaining': total_remaining,
    }
    return render(request, 'main/customer_detail.html', context)


def customer_row_edit(request, pk):
    row = get_object_or_404(CustomerRow, pk=pk)
    if request.method == 'POST':
        form = CustomerRowForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل الصف بنجاح')
            return redirect('customer_detail', pk=row.customer.pk)
    else:
        form = CustomerRowForm(instance=row)
    return render(request, 'main/customer_row_edit.html', {'form': form, 'row': row})


@require_POST
def customer_row_delete(request, pk):
    row = get_object_or_404(CustomerRow, pk=pk)
    customer_pk = row.customer.pk
    row.delete()
    messages.success(request, 'تم حذف الصف بنجاح')
    return redirect('customer_detail', pk=customer_pk)


def customer_print(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    rows = customer.rows.all()

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30,
                            leftMargin=30, topMargin=30, bottomMargin=30)

    elements = []

    title_text = get_display(reshape(f'الاسم: {customer.name}'))
    phone_text = get_display(reshape(f'رقم الهاتف: {customer.phone}'))

    title_para = Paragraph(
        f'<para align=right><b>{title_text}</b></para>', getSampleStyleSheet()['Normal'])
    phone_para = Paragraph(
        f'<para align=right><b>{phone_text}</b></para>', getSampleStyleSheet()['Normal'])

    elements.append(title_para)
    elements.append(phone_para)
    elements.append(Spacer(1, 0.2*inch))

    data = []
    headers = [get_display(reshape('الباقي')), get_display(reshape('واصل')),
               get_display(reshape('الأمتار')), get_display(reshape('المكان'))]
    data.append(headers)

    for row in rows:
        data.append([
            get_display(reshape(row.location)),
            str(row.meters),
            str(row.type) if row.type else '',
            str(row.received),
            str(row.remaining),
            str(row.date) if row.date else ''
        ])

    total_received = sum(row.received for row in rows)
    total_remaining = sum(row.remaining for row in rows)

    data.append([
        '',
        get_display(reshape('الإجمالي')),
        str(total_received),
        str(total_remaining)
    ])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
    ]))

    elements.append(table)
    doc.build(elements)

    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="customer_{customer.id}.pdf"'
    return response


def craftsman_list(request):
    craftsmen = Craftsman.objects.all()
    if request.method == 'POST':
        form = CraftsmanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة الأسطى بنجاح')
            return redirect('craftsman_list')
    else:
        form = CraftsmanForm()
    return render(request, 'main/craftsman_list.html', {'craftsmen': craftsmen, 'form': form})


def craftsman_detail(request, pk):
    craftsman = get_object_or_404(Craftsman, pk=pk)
    rows = craftsman.rows.all()

    if request.method == 'POST':
        form = CraftsmanRowForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.craftsman = craftsman
            row.order = craftsman.rows.count()
            row.save()
            messages.success(request, 'تم إضافة الصف بنجاح')
            return redirect('craftsman_detail', pk=pk)
    else:
        form = CraftsmanRowForm()

    context = {
        'craftsman': craftsman,
        'rows': rows,
        'form': form,
    }
    return render(request, 'main/craftsman_detail.html', context)


def craftsman_row_edit(request, pk):
    row = get_object_or_404(CraftsmanRow, pk=pk)
    if request.method == 'POST':
        form = CraftsmanRowForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل الصف بنجاح')
            return redirect('craftsman_detail', pk=row.craftsman.pk)
    else:
        form = CraftsmanRowForm(instance=row)
    return render(request, 'main/craftsman_row_edit.html', {'form': form, 'row': row})


@require_POST
def craftsman_row_delete(request, pk):
    row = get_object_or_404(CraftsmanRow, pk=pk)
    craftsman_pk = row.craftsman.pk
    row.delete()
    messages.success(request, 'تم حذف الصف بنجاح')
    return redirect('craftsman_detail', pk=craftsman_pk)


def worker_list(request):
    workers = Worker.objects.all()
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة العامل بنجاح')
            return redirect('worker_list')
    else:
        form = WorkerForm()
    return render(request, 'main/worker_list.html', {'workers': workers, 'form': form})


def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    rows = worker.rows.all()

    if request.method == 'POST':
        form = WorkerRowForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.worker = worker
            row.order = worker.rows.count()
            row.save()
            messages.success(request, 'تم إضافة الصف بنجاح')
            return redirect('worker_detail', pk=pk)
    else:
        form = WorkerRowForm()

    context = {
        'worker': worker,
        'rows': rows,
        'form': form,
    }
    return render(request, 'main/worker_detail.html', context)


def worker_row_edit(request, pk):
    row = get_object_or_404(WorkerRow, pk=pk)
    if request.method == 'POST':
        form = WorkerRowForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل الصف بنجاح')
            return redirect('worker_detail', pk=row.worker.pk)
    else:
        form = WorkerRowForm(instance=row)
    return render(request, 'main/worker_row_edit.html', {'form': form, 'row': row})


@require_POST
def worker_row_delete(request, pk):
    row = get_object_or_404(WorkerRow, pk=pk)
    worker_pk = row.worker.pk
    row.delete()
    messages.success(request, 'تم حذف الصف بنجاح')
    return redirect('worker_detail', pk=worker_pk)


def factory_detail(request):
    # Get or create the factory instance

    rows = FactoryRow.objects.all()

    # Calculate totals
    total_received = sum(row.received for row in rows)
    total_expenses = sum(row.expenses for row in rows)
    total_goods = sum(row.goods for row in rows)
    total_outgoing = sum(row.outgoing for row in rows)
    total_incoming = sum(row.incoming for row in rows)

    if request.method == 'POST':
        form = FactoryRowForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.order = rows.count()
            row.save()
            messages.success(request, 'تم إضافة الصف بنجاح')
            return redirect('factory_detail')
    else:
        form = FactoryRowForm()

    context = {
        'rows': rows,
        'form': form,
        'total_received': total_received,
        'total_expenses': total_expenses,
        'total_goods': total_goods,
        'total_outgoing': total_outgoing,
        'total_incoming': total_incoming,
    }
    return render(request, 'main/factory_detail.html', context)


def factory_row_edit(request, pk):
    row = get_object_or_404(FactoryRow, pk=pk)
    if request.method == 'POST':
        form = FactoryRowForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل الصف بنجاح')
            return redirect('factory_detail')
    else:
        form = FactoryRowForm(instance=row)
    return render(request, 'main/factory_row_edit.html', {'form': form, 'row': row})


@require_POST
def factory_row_delete(request, pk):
    row = get_object_or_404(FactoryRow, pk=pk)
    row.delete()
    messages.success(request, 'تم حذف الصف بنجاح')
    return redirect('factory_detail')
