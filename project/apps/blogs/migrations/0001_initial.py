# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('subscribers', models.ManyToManyField(related_name='subscribed_blogs', to=settings.AUTH_USER_MODEL, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('blog', models.ForeignKey(related_name='posts', to='blogs.Blog')),
            ],
            options={
                'ordering': ('-date_created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostReadMark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_read', models.BooleanField(default=True)),
                ('post', models.ForeignKey(related_name='post_read_marks', to='blogs.Post')),
                ('user', models.ForeignKey(related_name='post_read_marks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='postreadmark',
            unique_together=set([('user', 'post')]),
        ),
    ]
