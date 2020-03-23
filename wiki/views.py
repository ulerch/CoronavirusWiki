from django.shortcuts import render
from .models import Row, Column, WikiEntry

def wikiMatrix(request):
    context = {}
    context['cols'] = Column.objects.all()
    context['rows'] = Row.objects.all()

    return render(request, 'wiki/index.html', context)


def wikiList(request, rpk, cpk):
    r = Row.objects.get(pk=rpk)
    c = Column.objects.get(pk=cpk)
    context = {}
    context['title'] = r.label + ' - ' + c.label
    context['entries'] = WikiEntry.objects.filter(row=rpk, column=cpk)

    return render(request, 'wiki/list.html', context)
