from django.shortcuts import render, redirect
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
    context = {}
    context['row'] = rowPk;
    context['col'] = colPk;
    context['title'] = Row.objects.get(pk=rowPk).label + ': ' + Column.objects.get(pk=colPk).label
    context['entries'] = WikiEntry.objects.filter(row=rowPk, column=colPk)

    return render(request, 'wiki/list.html', context)


def wikiCreateView(request, rowPk, colPk):
    context = Row.objects.get(pk=rowPk).label + ': ' + Column.objects.get(pk=colPk).label
    initial = {'row': rowPk, 'column': colPk}
    if request.method == 'POST':
        form = CreateForm(request.POST, initial)
        if form.is_valid():
            #instance = form.save(commit=False)
            f_row = form.cleaned_data.get('row')
            f_column = form.cleaned_data.get('column')
            f_title = form.cleaned_data.get('title')
            f_text = form.cleaned_data.get('text')
            f_name = form.cleaned_data.get('name')
            f_email = form.cleaned_data.get('email')
            i_row = Row.objects.get(pk=f_row)
            i_column = Column.objects.get(pk=f_column)
            new = WikiEntry(
                row = i_row,
                column = i_column,
                title = f_title,
                text = f_text,
                contributor_name = f_name,
                contributor_email = f_email,
            )
            new.save()
            return redirect("/")
    else:
        form = CreateForm(initial)

    return render(request, 'wiki/create.html', {'form': form, 'title': context})
