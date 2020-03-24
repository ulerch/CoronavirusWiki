from django.shortcuts import render
from .models import Register, Row, Column, WikiEntry
from .forms import CreateForm


def register(request):
    return {'register': Register.objects.all()}


def wikiMatrix(request):
    context = {}
    regPk = Register.objects.get(position=1).pk;
    context['cols'] = Column.objects.filter(register=regPk)
    context['rows'] = Row.objects.filter(register=regPk)

    return render(request, 'wiki/index.html', context)


def wikiList(request, rowPk, colPk):
    r = Row.objects.get(pk=rowPk)
    c = Column.objects.get(pk=colPk)
    context = {}
    context['row'] = rowPk;
    context['col'] = colPk;
    context['title'] = r.label + ' - ' + c.label
    context['entries'] = WikiEntry.objects.filter(row=rowPk, column=colPk)

    return render(request, 'wiki/list.html', context)


def wikiCreateView(request, rowPk, colPk):
    r = Row.objects.get(pk=rowPk)
    c = Column.objects.get(pk=colPk)
    context = r.label + ' - ' + c.label
    initial = {'row': rowPk, 'column': colPk}
    if request.method == 'POST':
        form = CreateForm(request.POST, initial)
        if form.is_valid():
            pass
    else:
        form = CreateForm(initial)

    return render(request, 'wiki/create.html', {'form': form, 'title': context})
