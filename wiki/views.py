from django.shortcuts import render
from .models import Row, Column, WikiEntry
from .forms import CreateForm


def wikiMatrix(request):
    context = {}
    context['cols'] = Column.objects.all()
    context['rows'] = Row.objects.all()

    return render(request, 'wiki/index.html', context)


def wikiList(request, rpk, cpk):
    r = Row.objects.get(pk=rpk)
    c = Column.objects.get(pk=cpk)
    context = {}
    context['row'] = rpk;
    context['col'] = cpk;
    context['title'] = r.label + ' - ' + c.label
    context['entries'] = WikiEntry.objects.filter(row=rpk, column=cpk)

    return render(request, 'wiki/list.html', context)


def wikiCreateView(request, rpk, cpk):
    r = Row.objects.get(pk=rpk)
    c = Column.objects.get(pk=cpk)
    context = r.label + ' - ' + c.label
    initial = {'row': rpk, 'column': cpk}
    if request.method == 'POST':
        form = CreateForm(request.POST, initial)
        if form.is_valid():
            pass
    else:
        form = CreateForm(initial)

    return render(request, 'wiki/create.html', {'form': form, 'title': context})
