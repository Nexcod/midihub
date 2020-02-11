# Generated by Django 3.0.3 on 2020-02-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='midi',
            options={'ordering': ['-created_at'], 'verbose_name': 'MIDI file', 'verbose_name_plural': 'MIDI files'},
        ),
        migrations.AddField(
            model_name='midi',
            name='difficulty',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Very easy'), (1, 'Easy'), (2, 'Normal'), (3, 'Hard'), (4, 'Very hard')], default=2, verbose_name='Difficulty'),
        ),
        migrations.AlterField(
            model_name='midi',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='midi',
            name='file',
            field=models.FileField(upload_to='files/midi', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='midi',
            name='image',
            field=models.ImageField(upload_to='images/midi', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='midi',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='midi',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
