# Generated by Django 3.1.5 on 2021-02-20 17:56

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('tagme', '0002_forum_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]