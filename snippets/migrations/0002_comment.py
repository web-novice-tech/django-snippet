# Generated by Django 4.0 on 2022-02-12 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='本文')),
                ('commented_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.snippet', verbose_name='スニペット')),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='投稿者')),
            ],
        ),
    ]