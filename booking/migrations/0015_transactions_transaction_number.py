# Generated by Django 2.1.1 on 2018-11-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_guesthouse_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='transaction_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
