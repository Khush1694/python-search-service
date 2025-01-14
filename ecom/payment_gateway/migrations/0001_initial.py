# Generated by Django 3.0.7 on 2020-07-31 22:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentGateway',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('coupon_id', models.PositiveSmallIntegerField(blank=True, help_text='', null=True, verbose_name='installment')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_payment_gateway.paymentgateway_set+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'payment gateway',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('allow_installments', models.BooleanField(default=True, verbose_name='with installments')),
            ],
            options={
                'verbose_name': 'payment method',
            },
        ),
        migrations.CreateModel(
            name='PagarmeGateway',
            fields=[
                ('paymentgateway_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment_gateway.PaymentGateway')),
                ('api_key', models.CharField(max_length=255)),
                ('encryption_key', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Pagar.me',
                'verbose_name_plural': 'Pagar.me',
            },
            bases=('payment_gateway.paymentgateway',),
        ),
        migrations.CreateModel(
            name='PaymentMethodConfig',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('max_installments', models.SmallIntegerField(blank=True, help_text='If you do not allow installments, leave as 0', null=True, verbose_name='installment')),
                ('discount_percentage', models.PositiveSmallIntegerField(blank=True, help_text='In % (if not, leave it at 0)', null=True, verbose_name='installment')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payment_gateway.PaymentMethod', verbose_name='payment method')),
            ],
            options={
                'verbose_name': 'configuration of payment methods',
                'verbose_name_plural': 'configuration of payment methods',
            },
        ),
    ]
