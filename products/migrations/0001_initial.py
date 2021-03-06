# Generated by Django 3.2 on 2021-04-29 14:43

from django.db import migrations, models
import django.db.models.deletion
import products.p_models.image_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_user', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_user', models.IntegerField(blank=True, default=None, null=True)),
                ('name', models.CharField(default=None, max_length=40)),
                ('code', models.CharField(default=None, max_length=40)),
                ('description', models.CharField(default=None, max_length=120)),
            ],
            options={
                'db_table': 'brands',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_user', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_user', models.IntegerField(blank=True, default=None, null=True)),
                ('name', models.CharField(default=None, max_length=40)),
                ('code', models.CharField(default=None, max_length=40)),
                ('description', models.CharField(default=None, max_length=120)),
            ],
            options={
                'db_table': 'product_categorys',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('code', models.CharField(blank=True, default=None, max_length=30, null=True)),
            ],
            options={
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='OfferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=80, null=True)),
                ('code', models.CharField(default=None, max_length=80, null=True, unique=True)),
                ('discount', models.CharField(default=None, max_length=120, null=True)),
                ('from_date', models.DateTimeField(blank=True, null=True)),
                ('to_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Product Offers',
                'db_table': 'offers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=254, null=True, upload_to=products.p_models.image_model.uploadFolder)),
                ('source', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('size', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'product_image',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('code', models.CharField(blank=True, default=None, max_length=30, null=True)),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_user', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_user', models.IntegerField(blank=True, default=None, null=True)),
                ('name', models.CharField(default=None, max_length=50)),
                ('code', models.CharField(default=None, max_length=50)),
                ('description', models.CharField(default=None, max_length=120)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('images', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='products.pimage')),
            ],
            options={
                'db_table': 'product_subcategorys',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_user', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_user', models.IntegerField(blank=True, default=None, null=True)),
                ('title', models.CharField(default=None, max_length=80, null=True)),
                ('description', models.CharField(default=None, max_length=120, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('availability', models.BooleanField(blank=True, default=True, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('age_group', models.BooleanField(blank=True, default=True, null=True)),
                ('user', models.IntegerField(blank=True, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('colors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.colormodel')),
                ('images', models.ManyToManyField(blank=True, default=None, to='products.PImage')),
                ('offers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.offermodel')),
                ('sizes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.sizemodel')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.subcategory')),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='category',
            name='images',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.pimage'),
        ),
        migrations.AddField(
            model_name='brand',
            name='images',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.pimage'),
        ),
    ]
