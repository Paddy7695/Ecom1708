# Generated by Django 3.2.6 on 2021-08-22 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='customers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.customers'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='productimg'),
        ),
    ]
