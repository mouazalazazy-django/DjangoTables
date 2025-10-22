# Generated migration file
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='CustomerRow',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='CustomerRow',
            name='type',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='النوع'),
        ),
        migrations.AddField(
            model_name='CraftsmanRow',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AddField(
            model_name='CraftsmanRow',
            name='type',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='النوع'),
        ),
        migrations.AddField(
            model_name='WorkerRow',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='التاريخ'),
        ),
    ]