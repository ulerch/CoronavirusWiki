from django.shortcuts import render
from .models import Row, Column, WikiEntry

def wikiMatrix(request):
    context = {}
    context['cols'] = Column.objects.all()
    context['rows'] = Row.objects.all()

    for r in context['rows']:
        for c in context['cols']:
            res = WikiEntry.objects.filter(row=r.id, column=c.id).count()

    return render(request, 'wiki/index.html', context)
