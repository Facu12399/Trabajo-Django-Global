# Generated by Django 4.2.6 on 2023-10-26 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img_inventario')),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField(default=0)),
                ('origen', models.CharField(choices=[('NAC', 'Nacional'), ('IMP', 'Importado')], default='NAC', max_length=30)),
                ('categoria', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.categoria')),
            ],
            options={
                'verbose_name': 'Productos',
                'verbose_name_plural': 'Productos',
                'managed': True,
            },
        ),
    ]