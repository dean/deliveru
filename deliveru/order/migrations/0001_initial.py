# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_date', models.DateTimeField(verbose_name=b'date ordered')),
                ('order_details', models.CharField(max_length=2000)),
                ('user', models.ForeignKey(to='user_profile.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
