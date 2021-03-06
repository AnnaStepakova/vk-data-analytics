# Generated by Django 3.1.7 on 2021-04-04 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VKUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='report.vkuser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('from_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='report.vkuser')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='report.post')),
            ],
        ),
    ]
