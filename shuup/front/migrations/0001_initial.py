# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2016, Shuup Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.db import models, migrations
import shuup.core.fields
from django.conf import settings
import shuup.front.models.stored_basket


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoredBasket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('key', models.CharField(max_length=32, default=shuup.front.models.stored_basket.generate_key)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(db_index=True, auto_now=True)),
                ('persistent', models.BooleanField(db_index=True, default=False)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('finished', models.BooleanField(db_index=True, default=False)),
                ('title', models.CharField(max_length=64, blank=True)),
                ('data', shuup.core.fields.TaggedJSONField()),
                ('taxless_total', shuup.core.fields.MoneyValueField(max_digits=36, null=True, decimal_places=9, default=0, blank=True)),
                ('taxful_total', shuup.core.fields.MoneyValueField(max_digits=36, null=True, decimal_places=9, default=0, blank=True)),
                ('product_count', models.IntegerField(default=0)),
                ('owner_contact', models.ForeignKey(null=True, to='shuup.Contact', blank=True)),
                ('owner_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('products', models.ManyToManyField(to='shuup.Product', blank=True)),
            ],
        ),
    ]