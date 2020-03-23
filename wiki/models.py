from django.db import models
from ckeditor.fields import RichTextField


class Row(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    label = models.CharField(max_length=100, null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    position = models.PositiveIntegerField(null=False, blank=False)

    class Meta(object):
        ordering = ['position']
        verbose_name = 'Row'
        verbose_name_plural = 'Rows'

    def __str__(self):
        return "{} ({})".format(self.name, self.position)


class Column(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    label = models.CharField(max_length=100, null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    position = models.PositiveIntegerField(null=False, blank=False)

    class Meta(object):
        ordering = ['position']
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'

    def __str__(self):
        return "{} ({})".format(self.name, self.position)


class WikiEntry(models.Model):
    row = models.ForeignKey(Row, null=False, on_delete=models.CASCADE)
    column = models.ForeignKey(Column, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    text = RichTextField(null=True, blank=True)
    contributor_name = models.CharField(max_length=100, null=False, blank=False)
    contributor_email = models.EmailField(max_length=100, null=False, blank=False)
    position = models.PositiveIntegerField(null=False, blank=False)

    class Meta(object):
        ordering = ['row', 'column', 'position']
        verbose_name = 'WikiEntry'
        verbose_name_plural = 'WikiEntries'

    def save(self):
        super(WikiEntry, self).save()

    def __str__(self):
        return "{} ({}/{}-{})".format(self.title, self.row, self.column, self.position)